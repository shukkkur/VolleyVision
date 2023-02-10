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
  <code>University of Central Asia ⛰️</code>
</p>


<h2>🧪 Example usage</h2>

<p align="center">
  <img src="https://github.com/shukkkur/VolleyVision/blob/192abab595fb8252d7184a48d81fa3b5d5cd96a1/assets/rf_backview.gif" width=1000>
</p>


<h2>📝 About</h2>

<p><strong>7th November, 2022</strong> | The result of my project should be a web application, that takes a  volleyball video (small sized, single rally) and is able to detect and track the ball, players, the court and is able to provide game statistics.</p>


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
  pip install -r requirements.txt
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
