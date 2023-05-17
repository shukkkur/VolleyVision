import torch
import cv2, PIL
import numpy as np
import matplotlib.pyplot as plt
from models.yolo import Model
from utils.torch_utils import select_device
from typing import Generator, List, Tuple


def isint(s):
    p = '[-+]?\d+'
    return True if re.fullmatch(p, s) else False


def initialize_tracker(image, bbox):
    params = cv2.TrackerDaSiamRPN_Params()
    params.model = "DaSiamRPN/dasiamrpn_model.onnx"
    params.kernel_r1 = "DaSiamRPN/dasiamrpn_kernel_r1.onnx"
    params.kernel_cls1 = "DaSiamRPN/dasiamrpn_kernel_cls1.onnx"
    tracker = cv2.TrackerDaSiamRPN_create(params)

    while True:
        try:
            tracker.init(image, bbox)
        except Exception as e:
            print(e)
            continue

        return tracker


def generate_frames(video_file: str) -> Generator[np.ndarray, None, None]:
    '''
    frame_iterator = iter(generate_frames(video_file=SOURCE_VIDEO_PATH))
    frame = next(frame_iterator)
    '''
    video = cv2.VideoCapture(video_file)

    while video.isOpened():
        success, frame = video.read()

        if not success:
            break

        yield frame

    video.release()


def plot_image(image: np.ndarray, size: int = 12) -> None:
    plt.figure(figsize=(size, size))
    plt.imshow(image[...,::-1])
    plt.show()


def x_y_w_h(prediciton, model_name) -> Tuple:
    """
    - RoboFlow model returns the center of the bbox and its width and height
    - Yolov7/Pytorch model the upper left and the bottom right corners
    """
    if model_name == 'roboflow':
        try:
            x = int(prediciton.json()['predictions'][0]['x'])
            y = int(prediciton.json()['predictions'][0]['y'])
            w = int(prediciton.json()['predictions'][0]['width'])
            h = int(prediciton.json()['predictions'][0]['height'])
            
            x0, y0 = int(x - w / 2), int(y - h / 2)
            
            return x0, y0, w, h
        except:
            return (0, 0, 0, 0)

    elif model_name == 'yolov7':
        try:
            x_min, y_min, x_max, y_max, confidence, class_id = prediciton.pred[0].cpu().numpy()[0]
            x = int(x_min)
            y = int(y_min)
            w = int(x_max - x_min)
            h = int(y_max - y_min)
            return x, y, w, h
        except:
            return (0, 0, 0, 0)


def extract_coord(prediciton: dict) -> Tuple:
    x = int(prediciton.json()['predictions'][0]['x'])
    y = int(prediciton.json()['predictions'][0]['y'])
    w = int(prediciton.json()['predictions'][0]['width'])
    h = int(prediciton.json()['predictions'][0]['height'])

    x0, y0 = int(x - w / 2), int(y - h / 2)
    x1, y1 = int(x + w / 2), int(y + h / 2)
    
    return x0, y0, x1, y1 


def draw_box(src_img: np.ndarray, coords: Tuple, color=(255, 0, 0), thickness=2) -> np.ndarray:
    start_point = coords[0], coords[1]
    end_point = coords[2], coords[3]
    
    return cv2.rectangle(src_img, start_point, end_point, color, thickness)


def calc_distance(bbox1: Tuple[int, int, int, int],
                                bbox2: Tuple[int, int, int, int]):
    """
    Calculte Euclidean distance between two bbox
    """
    centr_x1, centr_y1 = calc_centroid(bbox1)
    centr_x2, centr_y2 = calc_centroid(bbox2)

    distance = np.sqrt((centr_x1 - centr_x2) ** 2 + (centr_y1 - centr_y2) ** 2)

    return distance


def calc_centroid(bbox):
    """
    Calculate the centroid of a given bounding box
    
    bbox should be a tuple of `x, y, w, h`:
    `(x, y)` - upper left coordinate of the bounding box
    `w` - width
    `h` - height 
    """
    centr_x = bbox[0] + bbox[2] / 2
    centr_y = bbox[1] + bbox[3] / 2

    return centr_x, centr_y


def PIL_to_cv2(img: PIL.Image):
    """
    Convert PIL image to OpenCV image
    """
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)


def custom(path_or_model='path/to/model.pt', autoshape=True):
    """custom mode

    Arguments (3 options):
        path_or_model (str): 'path/to/model.pt'
        path_or_model (dict): torch.load('path/to/model.pt')
        path_or_model (nn.Module): torch.load('path/to/model.pt')['model']

    Returns:
        pytorch model
    """
    model = torch.load(path_or_model, map_location=torch.device('cpu')) if isinstance(path_or_model, str) else path_or_model  # load checkpoint
    if isinstance(model, dict):
        model = model['ema' if model.get('ema') else 'model']  # load model

    hub_model = Model(model.yaml).to(next(model.parameters()).device)  # create
    hub_model.load_state_dict(model.float().state_dict())  # load state_dict
    hub_model.names = model.names  # class names
    if autoshape:
        hub_model = hub_model.autoshape()  # for file/URI/PIL/cv2/np inputs and NMS
    device = select_device('0' if torch.cuda.is_available() else 'cpu')  # default to GPU if available
    return hub_model.to(device)


class RoboYOLO:
    """
    Unified class for RoboFlow and yoloV7 models 
    """
    def __init__(self, model_name, model, confidence):
        self.name = model_name
        self.model = model
        self.conf = confidence

    def predict(self, frame):
        
        if self.name == 'roboflow':
            pred = self.model.predict(frame, confidence=self.conf)
            return pred

        elif self.name == 'yolov7':
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im_pil = PIL.Image.fromarray(img)

            pred = self.model(im_pil)
            return pred


def get_circle(bbox: Tuple[int, int, int, int]):
    """
    Get the centroid and the radius of bbox given
    the upper left corner and the width and heigh
    """
    x0, y0, w, h = bbox
    
    centr_x = int(x0 + w / 2)
    centr_y = int(y0 + h / 2)
    radius = int((w + h) / 4)

    return centr_x, centr_y, radius
