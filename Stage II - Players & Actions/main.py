import os
import cv2
import argparse
from ultralytics import YOLO

# Parse command-line arguments
parser = argparse.ArgumentParser(description='YOLOv8 Image/Video Processing')
parser.add_argument('--model', required=True, help="Path to model's weights")
parser.add_argument('--input_path', required=True, help='Path to the input image or video file')
parser.add_argument('--output_path', default='Output/output.jpg', help='Output directory path (for images) or output file path (for videos)')
parser.add_argument('--show_conf', default=False, action='store_true', help='Whether to show the confidence scores')
parser.add_argument('--show_labels', default=False, action='store_true', help='Whether to show the labels')
parser.add_argument('--conf', type=float, default=0.5, help='Object confidence threshold for detection')
parser.add_argument('--max_det', type=int, default=300, help='Maximum number of detections per image')
parser.add_argument('--classes', nargs='+', default=None, help='List of classes to detect')
parser.add_argument('--line_width', type=int, default=3, help='Line width for bounding box visualization')
parser.add_argument('--font_size', type=float, default=3, help='Font size for label visualization')
args = parser.parse_args()

# Load the YOLOv8 model
model = YOLO(args.model)

# Check if the input is an image or video
is_image = args.input_path.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))
is_video = args.input_path.endswith(('.mp4', '.avi', '.mkv', '.mov'))

if is_image:
    # Load and preprocess the image
    img = cv2.imread(args.input_path)

    # Perform prediction
    results = model(img,
                    conf=args.conf,
                    max_det=args.max_det,
                    classes=args.classes,
                    verbose=False)

    # Create the output directory if it doesn't exist
    try:
        os.makedirs(os.path.split(args.output_path)[0], exist_ok=True)
    except:
        pass

    # Annotate the image with bounding boxes
    annotated = results[0].plot(conf=args.show_conf,
                                labels=args.show_labels,
                                line_width=args.line_width,
                                font_size=args.font_size)

    # Save the annotated image
    cv2.imwrite(args.output_path, annotated)

elif is_video:
    # Open the video file
    cap = cv2.VideoCapture(args.input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_size = (
        int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    )

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.split(args.output_path)[0], exist_ok=True)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(args.output_path, fourcc, fps, frame_size)

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame,
                            conf=args.conf,
                            max_det=args.max_det,
                            classes=args.classes,
                            verbose=False)

            # Annotate the frame with bounding boxes
            annotated_frame = results[0].plot(conf=args.show_conf,
                                              labels=args.show_labels,
                                              line_width=args.line_width,
                                              font_size=args.font_size)

            # Write the annotated frame to the output video
            out.write(annotated_frame)

        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object, close the display window, and release the output video writer
    cap.release()
    cv2.destroyAllWindows()
    out.release()

else:
    raise ValueError("Invalid input format. Please provide either an image or a video file.")
