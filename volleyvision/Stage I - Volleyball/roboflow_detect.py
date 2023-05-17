import cv2
import os
import argparse
from my_utils import *
from tqdm import tqdm
from datetime import datetime
from roboflow import Roboflow

### Parse Arguments ###
parser = argparse.ArgumentParser()
parser.add_argument("--input_path",
                    type=str,
                    required=True,
                    help="path to the input video or image")
parser.add_argument("--output_path",
                    type=str,
                    default="Output/output.jpg",
                    help="path to save the output file")
parser.add_argument("--marker",
                    type=str,
                    default='circle',
                    choices=['circle', 'box'],
                    help="how to highlight the ball")
parser.add_argument("--color",
                    type=str,
                    default='yellow',
                    choices=['black', 'white', 'red', 'green', 'purple',
                             'blue', 'yellow', 'cyan', 'gray', 'navy'],
                    help="color for highlighting the ball")
args = parser.parse_args()

input_path = args.input_path
output_path = args.output_path
marker = args.marker
color = args.color

if color == 'yellow':
    color = [0, 255, 255]
elif color == 'black':
    color = [0, 0, 0]
elif color == 'white':
    color = [255, 255, 255]
elif color == 'red':
    color = [0, 0, 255]
elif color == 'green':
    color = [0, 255, 0]
elif color == 'blue':
    color = [255, 0, 0]
elif color == 'cyan':
    color = [255, 255, 0]
elif color == 'gray':
    color = [128, 128 ,128]
elif color == 'purple':
    color = [128, 0, 128]
elif color == 'navy':
    color = [128, 0, 0]

###################

### Model Selection ###
# Public API key, if it doesn't work, get it from -->
# https://universe.roboflow.com/volleyvision/volleyball-tracking/model/13
rf = Roboflow(api_key="WQp0964J9jw76po6tElU")
project = rf.workspace().project("volleyball-tracking")
model = project.version(18).model
###################

### Create Output Directory ###
output_dir = os.path.dirname(os.path.abspath(output_path))
os.makedirs(output_dir, exist_ok=True)
###################

### Process Image Function ###
def process_image(image_path):
    image = cv2.imread(image_path)
    debug_image = image.copy()

    pred = model.predict(image)
    bbox = x_y_w_h(pred, "roboflow")

    ### marker, color ###
    if bbox != (0, 0, 0, 0):
        if marker == 'box':
            cv2.rectangle(debug_image, bbox, color, thickness=2)
        elif marker == 'circle':
            *center, r = get_circle(bbox)
            cv2.circle(debug_image, center, r, color, 5)

    cv2.imwrite(output_path, debug_image)

### Process Video Function ###
def process_video(video_path):
    video_in = cv2.VideoCapture(video_path)

    if not video_in.isOpened():
        print("Error reading video file")
        return

    basename = os.path.basename(video_path)
    frame_width = int(video_in.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_in.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_in.get(cv2.CAP_PROP_FPS)

    video_out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    while video_in.isOpened():
        ret, frame = video_in.read()

        if not ret:
            break

        debug_frame = frame.copy()

        pred = model.predict(frame)
        bbox = x_y_w_h(pred, "roboflow")

        ### marker, color ###
        if bbox != (0, 0, 0, 0):
            if marker == 'box':
                cv2.rectangle(debug_frame, bbox, color, thickness=2)
            elif marker == 'circle':
                *center, r = get_circle(bbox)
                cv2.circle(debug_frame, center, r, color, 5)

        video_out.write(debug_frame)

    video_in.release()
    video_out.release()

# Check if the input path is a video or an image
if input_path.endswith(('.mp4', '.avi', '.mkv')):
    process_video(input_path)
else:
    process_image(input_path)
