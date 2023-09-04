<p align="center">
  <img src="https://github.com/shukkkur/VolleyVision/blob/b9e2ea29be1337f8cd7c25f7f06741ecfde9fc62/README_files/vv_logo.png" width=200>
</p>

<h1 align="center">
  Stage II - Players Detection & Action Recognition
</h1>

<p align='center'>
  <a href="https://ucentralasia.org/home"><code>University of Central Asia</a>⛰️</code>
</p>

<h2>🏃‍♂️ How to Run</h2>

<a href="https://colab.research.google.com/drive/1X16GNjksEfwVL1090bj3CYHGo772fG6H?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>

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
  cd VolleyVision\Stage II - Players & Actions
  pip install ultralytics
  ```

<li>
  <p>You can run using Python script <code>main.py</code></p>
</li>

1) ```python main.py --model actions/yV8_medium/weights/best.pt --input_path assets/actions.jpg --output_path Output/actions.jpg --show_labels```
2) ```python main.py --model players/yV8_medium/weights/best.pt --input_path assets/players.jpg --output_path Output/players.jpg```
  
  <li>
    <p>Since <a href="https://docs.ultralytics.com/quickstart/#use-with-cli">ultralytics</a> provides simple <strong>CLI</strong> you can also use it</p>
  </li>

1) ```yolo predict model=actions\yV8_medium\weights\best.pt source=assets\actions.jpg show_conf=False show_labels=True```
2) ```yolo predict model=players\yV8_medium\weights\best.pt source=assets\players.jpg show_conf=False show_labels=False```

<br>
  
|   <code>i.</code>   |   <code>ii.</code>   |
|--------------|--------------|
|  <img src="https://github.com/shukkkur/VolleyVision/blob/bd87bc614df0c6a2b38067b9d7e0c3a7603a4a65/Stage%20II%20-%20Players%20%26%20Actions/assets/out_actions.jpg" width="500">  |  <img src="https://github.com/shukkkur/VolleyVision/blob/b532943613057c9bc99f309434d622c2030235ad/Stage%20II%20-%20Players%20%26%20Actions/assets/out_players.jpg" width="500">  |


<h3>Action Recognition + Temporal Filtering = Event Detection</h3>

<p>For event detection I used the action recognition model, but now instead of drawing the bounding boxes on every frame, we intoduce temporal information using a list (deque). So, basically we store the last <code>N</code> frames' predictions and declare that an event occured only if a certain action has been predicted several times. Gosh, my explanation is terrible, please refer to below examples. </p>

```
# `-` means no detections
# `()` braces are the sliding window
# let's choose sliding_window of size `5`
# and threshold number of `3`, meaning we need 3 detections for an event to be declared

predictions = [-, -, spike, -, spike, spike, -, -, spike, spike]

[(-, -, spike, -, spike), spike, -, -, spike, spike]  # only two detections, no event
[-, (-, spike, -, spike, spike), -, -, spike, spike]  # yeah, we've got 3 detection within the window, draw "SPIKE" on top
[-, -, (spike, -, spike, spike, -), -, spike, spike]  # keep drawing/printing/declraing "SPIKE"
...
```

<p>I really hope this make sense now. Anyway, this simple, yet amazing idea belongs to my former mentor at BallerTV - <strong>Paul Kefer</strong>. Thank you for your patience))). 

<ol>
  <li>To run the event detection, use <code>sliding_window.py</code> script. </li>

```
!python sliding_wndow.py --model actions/yV8_medium/weights/best.pt --input_path "assets/rallies/rally.mp4" --output_path Output/event_detection.mp4 --conf 0.5
```
  <li>The effectiveness of this approach depends on confidence level (<code>--conf</code>), <a href="https://github.com/shukkkur/VolleyVision/blob/d0790a91c04ba04c5c25259e3abe18f19a55816d/Stage%20II%20-%20Players%20%26%20Actions/sliding_window_verbose.py#L55">sliding window size</a> and <a href="https://github.com/shukkkur/VolleyVision/blob/d0790a91c04ba04c5c25259e3abe18f19a55816d/Stage%20II%20-%20Players%20%26%20Actions/sliding_window_verbose.py#L157">threshhold</a>, so for experimental purposes use <code>sliding_window_verbose.py</code>. In addition to event, it also draws <code>[frame_number] (who's action/yellow circle) class_name (confidence)</code> </li>
  <li><code>--gpu</code> - for faster inference. Can be added to other scripts (do yourself). And <code>--imgsz</code> - to prevent <strong>YOLO</strong> resizing the input to <strong>640x640</strong> but instead to larger/smaller custom size.</li>

```
!python sliding_wndow_verbose.py --model actions/yV8_medium/weights/best.pt --input_path "assets/rallies/rally.mp4" --output_path Output/event_detection.mp4 --conf 0.4 --gpu --imgsz 1920 1080
```

</ol>

|   <code>sliding_window.py</code>   |   <code>sliding_window_verbose.py</code>   |
|--------------|--------------|
|  <img src="https://github.com/shukkkur/VolleyVision/blob/7cc0a1150273e7a0f1de8f50d741aba69f2339cc/Stage%20II%20-%20Players%20%26%20Actions/assets/sl_wind.png" width="500">  |  <img src="https://github.com/shukkkur/VolleyVision/blob/7cc0a1150273e7a0f1de8f50d741aba69f2339cc/Stage%20II%20-%20Players%20%26%20Actions/assets/sl_wind_verbose.png" width="500">  |


<p></p>

<h4>For any additional quesitons feel free to take part in <a href="https://github.com/shukkkur/VolleyVision/discussions">discussions</a>, open an <a href="https://github.com/shukkkur/VolleyVision/issues/new">issue</a> or <a href="https://github.com/shukkkur#feel-free-to-connectcontact">contact</a> me.</h4>

<img src="https://github.com/shukkkur/VolleyVision/blob/1d1836c3a7968cbcde4bcf5cfb5e8eaf4c16acfb/assets/header.png">
