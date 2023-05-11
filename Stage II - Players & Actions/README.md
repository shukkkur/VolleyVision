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
    <p>Since <a href="https://docs.ultralytics.com/quickstart/#use-with-cli">ultralytics</a> provides simple <strong>CLI</strong>, there is no need for Python environment.</p>
  </li>


|   <code>yolo predict model=actions\yV8_medium\weights\best.pt source=assets\players.jpg show_conf=False show_labels=False</code>   |   <code>yolo predict model=actions\yV8_medium\weights\best.pt source=assets\players.jpg show_conf=False show_labels=False</code>   |
|--------------|--------------|
|  ![Image 1](https://github.com/shukkkur/VolleyVision/blob/bd87bc614df0c6a2b38067b9d7e0c3a7603a4a65/Stage%20II%20-%20Players%20%26%20Actions/assets/out_actions.jpg)  |  ![Image 1](https://github.com/shukkkur/VolleyVision/blob/bd87bc614df0c6a2b38067b9d7e0c3a7603a4a65/Stage%20II%20-%20Players%20%26%20Actions/assets/out_actions.jpg)  |

 


<h4>For any additional quesitons feel free to take part in <a href="https://github.com/shukkkur/VolleyVision/discussions">discussions</a>, open an <a href="https://github.com/shukkkur/VolleyVision/issues/new">issue</a> or <a href="https://github.com/shukkkur#feel-free-to-connectcontact">contact</a> me.</h4>
