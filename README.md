<p align="center">
  <img src="https://github.com/shukkkur/VolleyVision/blob/b9e2ea29be1337f8cd7c25f7f06741ecfde9fc62/README_files/vv_logo.png" width=200>
</p>

<h1 align="center">
  👁️VolleyVision👁️
</h1>


<p align='center'>
  <img src="https://img.shields.io/github/forks/shukkkur/VolleyVision.svg">
  <img src="https://img.shields.io/github/stars/shukkkur/VolleyVision.svg">
  <img src="https://img.shields.io/github/watchers/shukkkur/VolleyVision.svg">
  
  <br>
  
  <img src="https://img.shields.io/github/last-commit/shukkkur/VolleyVision.svg">
  <img src="https://img.shields.io/badge/License-AGPL_v3-blue.svg">
  <img src="https://hits.sh/github.com/shukkkur/VolleyVision.svg"/>
  <br>
  
  <a href="https://universe.roboflow.com/shakhansho-sabzaliev/volleyball-tracking">
    <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
</a>
<a href="https://universe.roboflow.com/shakhansho-sabzaliev/volleyball-tracking/model/">
    <img src="https://app.roboflow.com/images/try-model-badge.svg"></img>
</a>

<br>
  <code>University of Central Asia ⛰️</code>
</p>


<h2>🧪 Example usage</h2>

<code>volleyball_15.mp4</code> | <code>back_view.mp4</code>
:-------------------------:|:-------------------------:
<img src="https://github.com/shukkkur/VolleyVision/blob/88474342fa4330ce268668986d9f5061d7ee8f6a/assets/y7Detect_volleyball15.gif"> | <img src="https://github.com/shukkkur/VolleyVision/blob/bcdc93c527d174e6bb22b5885b9267a819b39b59/assets/rf_backview.gif">


<h2>🎯 Objectives</h2>

<p>🏐 Learn and apply popular CV techniques to volleyball data
  <br>
  🏐 Popularize volleyball in the field of ML
  <br>
  🏐 Create volleyball datasets
  <br>
  🏐 Contirubte to open-soruce community
  <br>

</p>




<h2>📝 About</h2>

<p><strong>November 7, 2022</strong> | The result of my project should be a web application, that takes a  volleyball video (small sized, single rally) and is able to detect and track the ball, players, the court and is able to provide game statistics.</p>

<ul>
  
  <li>
    <h3>
      Stage I | Volleyball Tracking
    </h3>
  </li>
</ul>

<p>
<!--   <strong>February 10, 2023 </strong> -->
<!--    <i>Closing the first stage moderetly satisfied</i>.  -->
<!--   <br> -->
  Two trained models: <a href="https://blog.roboflow.com/new-and-improved-roboflow-train/">RoboFlow</a> (<a href="https://docs.roboflow.com/train">AutoML training</a>) and <a href="https://github.com/WongKinYiu/yolov7">yoloV7-tiny</a> (local training). Both were trained on my newly created <a href="https://universe.roboflow.com/volleyvision/volleyball-tracking/dataset/13">dataset</a> comprised of <strong>25k</strong> images of size <strong>640x640</strong>.  As for the tracker, <a href="https://github.com/foolwood/DaSiamRPN">DaSiamRPN</a> (<a href="https://docs.opencv.org/4.x/de/d93/classcv_1_1TrackerDaSiamRPN.html">cv2</a>) was used. If you are interested in the yolov7-tiny training process check out - <a href="https://wandb.ai/volleyvision/YOLOR/runs/2u30vyzp/overview?workspace=user-">wandb.ai</a>.
  <br><br>
  <strong>Metrics</strong>
  <br>
  <code>RoboFlow    - mAP 89.1% | precision 92.9% | recall 82.0%</code>
  <br>
  <code>yoloV7-tiny - mAP 74.1% | precision 86.4% | recall 65.8%</code>
  <br><br>

  <strong>RoboFlow</strong> model is more accurate and works better on official matches, rather than yolov7 model.However, it requires longer time for inference. Whereas, <strong>yoloV7-tiny</strong> is capable of real-time inference but is less accurate but still good for larger volleyballs. I was trying to train the standard <a href="https://github.com/WongKinYiu/yolov7#performance">yolov7</a>, however, with GPU memory being 4GB, I could only afford training with <code>--batch_size=8 --img-size=480</code>, which didn't yield good results.

  
<!--   https://blog.roboflow.com/new-and-improved-roboflow-train/ -->
</p>

<ul>
   <li>
    <h3>Stage II | Player Detection & Action Recognition</h3>
   </li>
</ul>

<p>
  In progress...
</p>

<ul>
   <li>
    <h3>Stage III | Court Tracking</h3>
   </li>
</ul>

<p>
  Someday ... 
</p>

<br>

<p>
<i><strong>For any additional quesitons feel free to <a href="https://github.com/shukkkur/VolleyVision/issues/new">open an issue</a> or <a href="https://api.whatsapp.com/send/?phone=79014077195&text&type=phone_number&app_absent=0">contact me</a></strong></i>
</p>

<h2>💾 Datasets</h2>

Ball            |  Players |  Court
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://github.com/shukkkur/VolleyVision/blob/6ac8230e48de95a8edb3a1c4793657ddb06f1409/README_files/volley-collage.jpg" width="500">  |  ![output_img1](https://github.com/shukkkur/VolleyVision/blob/2fa5999f2e69d2a21e80be2fb23f0bb59c861f4d/README_files/in_progress.jpg) |  ![output_img1](https://github.com/shukkkur/VolleyVision/blob/2fa5999f2e69d2a21e80be2fb23f0bb59c861f4d/README_files/in_progress.jpg)


<ul>
  <li>
  <a href="https://universe.roboflow.com/volleyvision/volleyball-tracking/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true">Volleyball</a> (1 class, annotated)
  <ul>
    <li>Source Images - <a href="https://universe.roboflow.com/volleyvision/volleyball-tracking/dataset/9">25k_version</a></li>
    <li>Source Images (640x640) - <a href="https://universe.roboflow.com/volleyvision/volleyball-tracking/dataset/13">25k_resized</a></li>
  </ul>
  </li>
  
  <li>
  Players
  <ul>
    <li>In Progress...</li>
  </ul>
  </li>
  
  <li>
    Court
    <ul>
      <li>In Progress...</li>
    </ul>
  </li>
  
</ul>

<h2>🏃‍♂️ How to Run</h2>

<ol>
  
  <li>
    Clone this repository
  </li>
  
  ```
  git clone https://github.com/shukkkur/VolleyVision.git
  ```
  
  <li>
    Install the requirements
  </li>
  
  ```
  cd VolleyVision
  pip install -r requirements.txt
  ```
  
  Let's test on <a href="https://github.com/shukkkur/VolleyVision/blob/a87326441528ee89f4d23a81e2461d6963534134/assets/rally_men.mp4">assets/rally_men.mp4</a>. It's a <strong>5 seconds video that weights about 5.2 MB</strong>
  
  <li>
    If you want to get <strong>faster results</strong>, than use <code>volley_track.py</code> which utilizes a model in combination with DaSiamRPN tracker
  </li>
  
  ```
  python volley_track.py --input_video_path assets\rally_men.mp4 --model roboflow --marker circle --color yellow
  ```
  
  <li>
    Elif <strong>accuracy</strong> is what you are after, use <code>volley_detect.py</code>. It calls the model on every frame.
  </li>
  
  ```
  python volley_detect.py --input_video_path assets\rally_men.mp4 --model roboflow --marker circle --color yellow 
  ```
  
  
  <code>volley_track.py</code>  | <code>volley_detect.py</code>
:-------------------------:|:-------------------------:
<img src="https://github.com/shukkkur/VolleyVision/blob/a87326441528ee89f4d23a81e2461d6963534134/assets/track_men.gif"> | <img src="https://github.com/shukkkur/VolleyVision/blob/a87326441528ee89f4d23a81e2461d6963534134/assets/rf_rallyMen.gif">

  <i>Note that, it took <code>volley_track.py</code> <strong>0.73</strong> minutes to process the video, whereas <code>volley_dtect.py</code> completed in <strong>2.75 minutes</strong>.</i>

<li>
  If you are interested in running the models on individual frames, for <code>roboflow</code> use this <a href="https://universe.roboflow.com/volleyvision/volleyball-tracking/model/13">API</a>. And for <code>yolov7-tiny</code> run the following line with <code>--source</code> being your image, folder with images or even video.
</li>

```
python detect.py --weights best.pt --conf 0.5 --source assets/small
```

<h3>Acknowledgement</h3>

<details><summary> <b>Expand</b> </summary>
  <ul>
    <li>
    This project wouldn't possible without amazing & free RoboFlow <a href="https://roboflow.com/annotate">annotation tools</a> , open-source <a href="https://universe.roboflow.com/">datasets</a>, quick & easy <a href="https://roboflow.com/deploy">deployement</a> and high-level <a href="https://blog.roboflow.com/">blog posts</a></li>
  <li>Supervisor</li>
  <li>Course Instructor</li>
  <li>University of Central Asia</li>
  </ul>
</details>


<!--
<table>
<tr>
<td> Status </td> <td> Response </td>
</tr>
<tr>
<td> 200 </td>
<td>

```python
from roboflow import Roboflow
rf = Roboflow(api_key="sparlyxRfGqxvrUwHldB")
project = rf.workspace().project("radardata")
model = project.version(1).model

# infer on a local image
print(model.predict("your_image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
```
V Extra blank line below!

</td>
</tr>
<tr>
<td> 400 </td>
<td>

**Markdown** _here_. (Blank lines needed before and after!)

</td>
</tr>
</table>
-->
