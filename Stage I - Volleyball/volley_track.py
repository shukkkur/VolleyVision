import cv2
import torch
import queue
import os
import sys
import argparse
import warnings
import time
import copy
from my_utils import *
from tqdm import tqdm
from datetime import datetime
from roboflow import Roboflow


###   supress warnings  ###
warnings.filterwarnings("ignore")
###################


### Parse Arguments ###
parser = argparse.ArgumentParser()

parser.add_argument("--input_video_path",
                    type=str,
                    default="assets/back_view.mp4",
                    help="path to the video with volleyball in it")
parser.add_argument("--output_video_path",
                    type=str,
                    default="",
                    help="path for the output video (.mp4), default new VideoOutput folder")
parser.add_argument("--model",
                    type=str,
                    default='roboflow',
                    choices=['roboflow', 'yolov7'],
                    help="which model to use for prediction")
parser.add_argument("--confidence",
                    type=float,
                    default=0.2,
                    help="prediction confidence")
parser.add_argument("--show",
                    action='store_true',
                    help="watch preview")
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
parser.add_argument("--no_trace",
                    action='store_true',
                    help="don't draw trajectory of the ball")

args = parser.parse_args()
input_video = args.input_video_path
output_video = args.output_video_path
model_name = args.model
conf = args.confidence
show = args.show
marker = args.marker
no_trace = args.no_trace
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
    color = [128, 128, 128]
elif color == 'purple':
    color = [128, 0, 128]
elif color == 'navy':
    color = [128, 0, 0]
###################


###    Start Time    ###
t1 = datetime.now()
###################


### Capture Video ###
video_in = cv2.VideoCapture(input_video)

if (video_in.isOpened() == False):
    print("Error reading video file")
###################


### Video Writer ###
basename = os.path.basename(input_video)
extension = os.path.splitext(output_video)[1]

if output_video == "":  #
    os.makedirs('VideoOutput', exist_ok=True)
    output_video = os.path.join(
        "VideoOutput", model_name + 'Track' + '_' + basename)
else:  # check if user path exists, create otherwise
    f = os.path.split(output_video)[0]
    if not os.path.isdir(f):
        os.makedirs(f)

if (extension != '.mp4') and (extension != ''):
    raise Exception(
        f"Extention for output video should be `.mp4`, but got {extension}")

fname = output_video
fps = video_in.get(5)
frame_width = int(video_in.get(3))
frame_height = int(video_in.get(4))
dims = (frame_width, frame_height)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
total_frames = video_in.get(cv2.CAP_PROP_FRAME_COUNT)
video_out = cv2.VideoWriter(fname, fourcc, fps, dims)
###################


### Model Selection ###
if model_name == 'roboflow':
    #  API key, if doesn't work, refer -->
    #  https://github.com/shukkkur/VolleyVision/discussions/5#discussioncomment-7737081
    rf = Roboflow(api_key="INSERT YOUR OWN API_KEY")
    project = rf.workspace().project("volleyball-tracking")
    model = project.version(13).model
elif model_name == 'yolov7':
    model = custom(path_or_model='yV7-tiny/weights/best.pt')
    model.conf = conf

model = RoboYOLO(model_name, model, conf)
###################


### Find Desired Object ####
bbox = (0, 0, 0, 0)

while bbox == (0, 0, 0, 0):
    ret, frame = video_in.read()
    if not ret:
        break

    pred = model.predict(frame)
    bbox = x_y_w_h(pred, model_name)

if bbox == (0, 0, 0, 0):
    raise Exception(
        "Processed the whole video but failed to detect any volleyball")
###################


### Trajectory of volleyball ###
q = queue.deque()  # we need to save the coordinate of previous 7 frames
for i in range(0, 8):
    q.appendleft(None)

q.appendleft(bbox)
###################


### Initialize Tracker ###
ok, image = video_in.read()   # get first frame
tracker = initialize_tracker(image, bbox)  # image, bounding box
###################


### Flag Variables & Progress Bar ###
previous = bbox
counter = 0
pbar = tqdm(total=int(total_frames),
            bar_format='Processing: {desc}{percentage:3.0f}%|{bar:10}')
###################


### Process Video & Write Frames ###
while video_in.isOpened():

    ret, image = video_in.read()
    if not ret:
        break
    debug_image = copy.deepcopy(image)

    # Update Progress Bar
    pbar.update(1)

    # Updating Tracker
    ok, bbox = tracker.update(image)
    counter += 1

    if counter == 10:
        #  calculate Euclidean Distance
        #  between bbox 10 frames apart
        distance = calc_distance(previous, bbox)
        previous = bbox

    if ok:
        if counter < 10:
            q.appendleft(bbox)
            q.pop()
        else:
            if distance > 50:
                #  significant change in bbox location / all good
                q.appendleft(bbox)
                q.pop()
                counter = 0
            else:
                #  bbox hasn't moved / stuck on non-volleyball object
                #  since we know that volleyball woud always be in motion
                pred = model.predict(image)
                bbox = x_y_w_h(pred, model_name)
                q.appendleft(bbox)
                q.pop()
                counter = 0

                if bbox != (0, 0, 0, 0):
                    tracker = initialize_tracker(image, bbox)
                    previous = bbox
                else:
                    q.appendleft(None)
                    q.pop()

    ### marker, color & trace ###
    for i in range(0, 8):
        if q[i] is not None:

            if i == 0:  # current detection
                if marker == 'box':
                    cv2.rectangle(debug_image, q[i], color, thickness=2)
                elif marker == 'circle':
                    *center, r = get_circle(q[i])
                    cv2.circle(debug_image, center, r, color, 5)

            elif (i != 0) and (no_trace is False):  # pass detections
                if marker == 'box':
                    cv2.rectangle(debug_image, q[i], color, thickness=2)
                elif marker == 'circle':
                    *center, r = get_circle(q[i])
                    try:
                        cv2.circle(debug_image, center, r-10, color, -1)
                    except:
                        cv2.circle(debug_image, center, r, color, -1)
    ###################

    video_out.write(debug_image)
###################
    if show:
        cv2.imshow('"p" - PAUSE, "Esc" - EXIT', debug_image)

    k = cv2.waitKey(1)
    if k == ord('p'):
        cv2.waitKey(-1)  # PAUSE
    if k == 27:  # ESC
        break

video_in.release()
video_out.release()
cv2.destroyAllWindows()
pbar.close()

###     End Time     ###
t2 = datetime.now()
dt = t2 - t1
###################
print(f'Done - {dt.seconds/60:.2f} minutes')
