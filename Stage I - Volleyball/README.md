<p align="center">
  <img src="https://github.com/shukkkur/VolleyVision/blob/b9e2ea29be1337f8cd7c25f7f06741ecfde9fc62/README_files/vv_logo.png" width=200>
</p>

<h1 align="center">
  Volleyball Detection & Tracking
</h1>

<p align='center'>
  <a href="https://ucentralasia.org/home"><code>University of Central Asia</a>⛰️</code>
</p>

<h2>🏃‍♂️ How to Run</h2>


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1X16GNjksEfwVL1090bj3CYHGo772fG6H?usp=sharing)


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
  cd VolleyVision\Stage I - Volleyball
  pip install -r requirements.txt
  ```

  <li>❗If you are facing errors when trying to use <strong>RoboFlow model</strong>, please refer to this <a href="https://github.com/shukkkur/VolleyVision/discussions/5#discussioncomment-7737081">disscusion</a></li>

  <h3 align="center"><code>MODELS</code><br><code>"yolov7" - fast | "roboflow" - accurate</code></h3>
  
  Let us test on <a href="https://github.com/shukkkur/VolleyVision/blob/a87326441528ee89f4d23a81e2461d6963534134/assets/rally_men.mp4">assets/rally_men.mp4</a>. It's a 5 seconds video that weights about 5.2 MB.
  
  <li>
    If you want to get <strong>fast results</strong>, use <strong>volley_track.py</strong> which utilizes a model in combination with DaSiamRPN tracker
  </li>
  
  ```
  python volley_track.py --input_path assets\rally_men.mp4 --input_type video --onput_video_path Output/track.mp4 --model roboflow --marker circle --color yellow
  ```
  
  <li>
    Elif <strong>accuracy</strong> is what you are after, use <strong>detect.py</strong>. It calls the model on every frame.
  </li>
  
  ```
  python detect.py --input_path assets\rally_men.mp4 --input_type video --output_path Output/detect.mp4--model roboflow --marker circle --color yellow 
  ```
  
  
<strong>Output/track.mp4</strong>  | <strong>Output/detect.mp4</strong>
:-------------------------:|:-------------------------:
<img src="https://github.com/shukkkur/VolleyVision/blob/914b8dc3873767b7b1a1c62b7b75633d8a3a9af6/assets/track_men.gif"> | <img src="https://github.com/shukkkur/VolleyVision/blob/280fed79d290c1cf6d53c869fa60355eeb04d148/assets/rf_men_rally.gif">

<i>Note that, it took <code>volley_track.py</code> <strong>0.73</strong> minutes to process the video, whereas <strong>detect.py</strong> completed in <strong>2.75 minutes</strong>.</i>

<ul>
  <li>
    <p>You can get all list or arguments using <code>-h</code>code> flag</p>
  </li>
</ul>

```python
python detect.py -h
```

<img src="https://github.com/shukkkur/VolleyVision/blob/210368ae91bd078d2f00dfbbbe020f59625c2550/Stage%20I%20-%20Volleyball/assets/args.png">


<h4>For any additional quesitons feel free to take part in <a href="https://github.com/shukkkur/VolleyVision/discussions">discussions</a>, open an <a href="https://github.com/shukkkur/VolleyVision/issues/new">issue</a> or <a href="https://github.com/shukkkur#feel-free-to-connectcontact">contact</a> me.</h4>

<a href="https://github.com/shukkkur/VolleyVision/discussions">
<img src="https://github.com/shukkkur/VolleyVision/blob/1d1836c3a7968cbcde4bcf5cfb5e8eaf4c16acfb/assets/header.png">
</a>
