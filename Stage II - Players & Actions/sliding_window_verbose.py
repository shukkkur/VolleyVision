import os
import cv2
import torch
import argparse
from ultralytics import YOLO
from collections import deque, Counter

import warnings
warnings.filterwarnings("ignore")


# Parse command-line arguments
parser = argparse.ArgumentParser(description='YOLOv8 Image/Video Processing')
parser.add_argument('--model', required=True, help="Path to model's weights")
parser.add_argument('--input_path', required=True,
                    help='Path to the input image or video file')
parser.add_argument('--output_path', default='Output/output.jpg',
                    help='Output directory path (for images) or output file path (for videos)')
parser.add_argument('--show_conf', default=False, action='store_true',
                    help='Whether to show the confidence scores')
parser.add_argument('--show_labels', default=False,
                    action='store_true', help='Whether to show the labels')
parser.add_argument('--conf', type=float, default=0.5,
                    help='Object confidence threshold for detection')
parser.add_argument('--max_det', type=int, default=300,
                    help='Maximum number of detections per image')
parser.add_argument('--classes', nargs='+', default=None,
                    help='List of classes to detect')
parser.add_argument('--line_width', type=int, default=3,
                    help='Line width for bounding box visualization')
parser.add_argument('--font_size', type=float, default=3,
                    help='Font size for label visualization')
parser.add_argument('--verbose', default=False, action='store_true',
                    help='Print the predicted results information')
parser.add_argument('--imgsz', nargs=2, type=int, default=None,
                    help='Model inference resolution `width height`')
parser.add_argument('--gpu', default=False,
                    action='store_true', help='Whether to use GPU')
args = parser.parse_args()

if args.gpu:
    torch.cuda.set_device(0)

# Load the YOLOv8 model
model = YOLO(args.model)
classes = {0: 'block', 1: 'defense', 2: 'serve', 3: 'set', 4: 'spike'}

formats = ('.mp4', '.avi', '.mkv', '.mov', '.mpv')
is_video = args.input_path.endswith(formats)


if is_video:
    # Open the video file
    cap = cv2.VideoCapture(args.input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_size = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.split(args.output_path)[0], exist_ok=True)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(args.output_path, fourcc, fps, frame_size)

    event_list = deque(maxlen=10)  # verbose info at the top of the frame
    event_detected = deque(maxlen=15)  # what to display for the next 15 frames
    sliding_window = deque(maxlen=10)  # sliding window of 5 frames

    # Event will be declared when
    # the event_counter exceeds 3
    event = False
    event_counter = 0

    # Loop through the video frames
    frame_num = 1
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            if args.imgsz:
                results = model.predict(frame,
                                        imgsz=args.imgsz,
                                        conf=args.conf,
                                        max_det=args.max_det,
                                        classes=args.classes,
                                        verbose=args.verbose)
            else:
                results = model.predict(frame,
                                        conf=args.conf,
                                        max_det=args.max_det,
                                        classes=args.classes,
                                        verbose=args.verbose)

            annotated_frame = frame.copy()

            # Annotate the frame with bounding boxes
            # annotated_frame = results[0].plot(conf=args.show_conf,
            #                                 labels=args.show_labels,
            #                                 line_width=args.line_width,
            #                                 font_size=args.font_size)

            # Annotate the image with bounding boxes and frame number
            # Draw the frame number at the bottom-left corner of the frame
            frame_num_text = f"Frame: {frame_num}"
            text_color = (255, 255, 255)  # white text
            bg_color = (0, 0, 0)  # black background
            font_scale = 2  # 1.0
            thickness = 2  # 1
            font = cv2.FONT_HERSHEY_SIMPLEX
            text_size, _ = cv2.getTextSize(
                frame_num_text, font, font_scale, thickness)
            # For 720p video
            # text_x = 10
            # text_y = annotated_frame.shape[0] - 10
            # cv2.rectangle(annotated_frame, (text_x, text_y - text_size[1]), (text_x + text_size[0], text_y), bg_color, -1)
            # cv2.putText(annotated_frame, frame_num_text, (text_x, text_y), font, font_scale, text_color, thickness)
            # For 2160p video
            cv2.rectangle(annotated_frame, (0, 2080),
                          (text_size[0]+15, 2160), bg_color, -1)
            cv2.putText(annotated_frame, frame_num_text, (10,
                        frame.shape[0]-10), font, font_scale, text_color, thickness)

            # Update the event list with the current frame's detections
            boxes = results[0].boxes

            if len(boxes) > 0:
                for box in boxes:
                    x_min, y_min, x_max, y_max = box.xyxy[0]

                    center_x = (x_min + x_max) / 2
                    center_y = (y_min + y_max) / 2

                    event_str = f"[{frame_num}] {(int(center_x), int(center_y))} {classes[int(box.cls)]} ({float(box.conf):.2f}) "
                    cv2.circle(annotated_frame, (int(center_x),
                               int(center_y)), 20, (0, 255, 255), -1)
            else:
                event_str = f"[{frame_num}] - "

            event_list.append(event_str)

            # Draw the event list at the top of the frame
            event_text = " ".join(list(event_list))
            font_scale = 2  # 0.8
            text_color = (255, 255, 255)  # white text
            thickness = 2  # 1
            font = cv2.FONT_HERSHEY_SIMPLEX
            text_size, _ = cv2.getTextSize(
                event_text, font, font_scale, thickness)
            text_x = 20  # 10
            text_y = 80  # 30
            line1 = event_text[:len(event_text)//2].strip()
            line2 = event_text[len(event_text)//2:].strip()
            bg_color = (0, 0, 0)  # black background
            # For 720p video
            # cv2.rectangle(annotated_frame, (0, 0), (1440, 90), bg_color, -1)
            # cv2.putText(annotated_frame, line1, (text_x, text_y), font, font_scale, text_color, thickness)
            # cv2.putText(annotated_frame, line2, (text_x, text_y + int(2.5 * text_size[1])), font, font_scale, text_color, thickness)
            # For 2160p video
            cv2.rectangle(annotated_frame, (0, 0), (3840, 220), bg_color, -1)
            cv2.putText(annotated_frame, line1, (text_x, text_y),
                        font, font_scale, text_color, thickness)
            cv2.putText(annotated_frame, line2, (text_x, text_y + int(2.5 *
                        text_size[1])), font, font_scale, text_color, thickness)

            # Check if there is a detection in the current frame
            if len(results[0]) > 0:
                # class names of all detections
                cls = [classes[int(idx)]
                       for idx in results[0].boxes.cls.tolist()]
                sliding_window.extend(cls)
                cls, count = Counter(sliding_window).most_common(1)[0]

                if (count >= 5) and (cls != None):
                    event = True
            else:
                sliding_window.append(None)

            # If event detected 5 times, announce
            if event:
                event = False
                for i in range(15):
                    event_detected.append(cls)

            try:
                # Draw the event detected at the bottom of the frame
                event_msg = f"{event_detected.popleft()}".upper()
                text_size, _ = cv2.getTextSize(
                    event_msg, font, font_scale, thickness)
                text_x = (annotated_frame.shape[1] - text_size[0]) // 2
                text_y = 220
                cv2.rectangle(annotated_frame, (text_x-20, text_y), (text_x +
                              text_size[0]+150, text_y + text_size[1]+80), (0, 0, 255), -1)
                cv2.putText(annotated_frame, event_msg,
                            (text_x, text_y+80), font, 3, (255, 255, 255), 2)
            except IndexError:
                pass

            # Write the annotated frame to the output video
            out.write(annotated_frame)
            frame_num += 1
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object, close the display window, and release the output video writer
    cap.release()
    cv2.destroyAllWindows()
    out.release()

else:
    raise ValueError(
        f"Invalid input format. Please provide one from: {formats}")
