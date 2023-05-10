<p align="center">
  <img src="https://github.com/shukkkur/VolleyVision/blob/b9e2ea29be1337f8cd7c25f7f06741ecfde9fc62/README_files/vv_logo.png" width=200>
</p>

<h1 align="center">
  Volleyball Detection & Tracking
</h1>

<p align='center'>
  <code>University of Central Asia ⛰️</code>
</p>

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
<img src="https://github.com/shukkkur/VolleyVision/blob/914b8dc3873767b7b1a1c62b7b75633d8a3a9af6/assets/track_men.gif"> | <img src="https://github.com/shukkkur/VolleyVision/blob/280fed79d290c1cf6d53c869fa60355eeb04d148/assets/rf_men_rally.gif">

  <i>Note that, it took <code>volley_track.py</code> <strong>0.73</strong> minutes to process the video, whereas <code>volley_dtect.py</code> completed in <strong>2.75 minutes</strong>.</i>

<li>
  If you are interested in running the models on individual frames, for <code>roboflow</code> use this <a href="https://universe.roboflow.com/volleyvision/volleyball-tracking/model/13">API</a>. And for <code>yolov7-tiny</code> run the following line with <code>--source</code> being your image, folder with images or even video.
</li>

```
python detect.py --weights best.pt --conf 0.5 --source assets/small
```
