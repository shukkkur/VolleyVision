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

1) ```python main.py --model actions\yV8_medium\weights\best.pt --input_path assets\actions.jpg --ouput_path Output/actions.jpg --show_labels```
2) ```python main.py --mode players\yV8_medium\weights\best.pt --input_path assets\players.jpg --ouput_path Output/players.jpg```
  
  <li>
    <p>Since <a href="https://docs.ultralytics.com/quickstart/#use-with-cli">ultralytics</a> provides simple <strong>CLI</strong> you can also use it</p>
  </li>

1) ```yolo predict model=actions\yV8_medium\weights\best.pt source=assets\actions.jpg show_conf=False show_labels=True```
2) ```yolo predict model=players\yV8_medium\weights\best.pt source=assets\players.jpg show_conf=False show_labels=False```

<br>
  
|   <code>i.</code>   |   <code>ii.</code>   |
|--------------|--------------|
|  <img src="https://github.com/shukkkur/VolleyVision/blob/bd87bc614df0c6a2b38067b9d7e0c3a7603a4a65/Stage%20II%20-%20Players%20%26%20Actions/assets/out_actions.jpg" width="500">  |  <img src="https://github.com/shukkkur/VolleyVision/blob/b532943613057c9bc99f309434d622c2030235ad/Stage%20II%20-%20Players%20%26%20Actions/assets/out_players.jpg" width="500">  |

 


<h4>For any additional quesitons feel free to take part in <a href="https://github.com/shukkkur/VolleyVision/discussions">discussions</a>, open an <a href="https://github.com/shukkkur/VolleyVision/issues/new">issue</a> or <a href="https://github.com/shukkkur#feel-free-to-connectcontact">contact</a> me.</h4>
