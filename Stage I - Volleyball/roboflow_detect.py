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
                    help="path to the input image or folder with images")
parser.add_argument("--output_path",
                    type=str,
                    default="Output",
                    help="path to save the output images")
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
os.makedirs(output_path, exist_ok=True)
###################

### Process Image Function ###
def process_image(image_path):
    image_name = os.path.basename(image_path)
    output_image_path = os.path.join(output_path, image_name)
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

    cv2.imwrite(output_image_path, debug_image)
    ###################

### Process Images in Input Path ###
if os.path.isfile(input_path):  # Single image
    process_image(input_path)
elif os.path.isdir(input_path):  # Folder with images
    image_files = [f for f in os.listdir(input_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    total_images = len(image_files)
    pbar = tqdm(total=total_images, bar_format='Processing: {desc}{percentage:3.0f}%|{bar:10}')

    for image_file in image_files:
        image_path = os.path.join(input_path, image_file)
        process_image(image_path)

        # Update progress bar
        pbar.update(1)

    pbar.close()
else:
    print("Invalid input path. Please provide a valid path to an image or a folder with images.")
