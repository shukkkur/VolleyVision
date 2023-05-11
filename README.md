<p align="center">
  <img src="https://github.com/shukkkur/VolleyVision/blob/280fed79d290c1cf6d53c869fa60355eeb04d148/assets/vv_logo.png" width=200>
</p>

<h1 align="center">
  👁️VolleyVision👁️
</h1>


<p align='center'>
  <a href="https://github.com/shukkkur/VolleyVision/forks?include=active%2Carchived%2Cinactive%2Cnetwork&page=1&period=2y&sort_by=stargazer_counts"><img src="https://img.shields.io/github/forks/shukkkur/VolleyVision.svg"></a>
  <a href="https://github.com/shukkkur/VolleyVision/stargazers"><img src="https://img.shields.io/github/stars/shukkkur/VolleyVision.svg"></a>
  <a href="https://github.com/shukkkur/VolleyVision/watchers"><img src="https://img.shields.io/github/watchers/shukkkur/VolleyVision.svg"></a>
 
  <br>
  <a href=""><img src="https://img.shields.io/github/last-commit/shukkkur/VolleyVision.svg"></a>
  <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img src="https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg"></a>
  <img src="https://hits.sh/github.com/shukkkur/VolleyVision.svg"/>
  
  <br>
  <a href="https://ucentralasia.org/home"><code>University of Central Asia</a>⛰️</code>
  
</p>


<h2>🧪 Example usage</h2>

Sample Inputs | From [assets/](https://github.com/shukkkur/VolleyVision/tree/main/Stage%20I%20-%20Volleyball/assets)
:-------------------------:|:-------------------------:
<a href="https://github.com/shukkkur/VolleyVision/tree/main/Stage%20I%20-%20Volleyball/weights/weights"><img src="https://github.com/shukkkur/VolleyVision/blob/88474342fa4330ce268668986d9f5061d7ee8f6a/assets/y7Detect_volleyball15.gif" width="385" height="250"></a> | <a href="https://github.com/shukkkur/VolleyVision/tree/main/Stage%20I%20-%20Volleyball/weights/weights"><img src="https://github.com/shukkkur/VolleyVision/blob/eb639742363fb5564d6de4c3b1bf3da808162aa9/assets/rf_backview.gif" width="385" height="250"></a>
<strong>Action Recognition</strong> | <strong>Players Detection</strong>
<a href="https://github.com/shukkkur/VolleyVision/tree/main/Stage%20II%20-%20Players%20%26%20Actions/weights/actions/yV8_medium/weights"><img src="https://github.com/shukkkur/VolleyVision/blob/1c6c180c445a8be413defac520899e411c07f043/assets/actions.gif" width="385" height="250"></a> | <a href="https://github.com/shukkkur/VolleyVision/tree/main/Stage%20II%20-%20Players%20%26%20Actions/weights/players/yV8_medium/weights"><img src="https://github.com/shukkkur/VolleyVision/blob/aae563828d54dd16f68c75518e3e3a18c14f2092/assets/players_screen.jpg" width="385" height="250"></a>


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

<p><strong>November 7, 2022</strong> | The result of my project should be a web application, that takes a  volleyball video  and is able to detect and track the ball, players, the court and provides game statistics.</p>


<details><summary><h3>Stage I | Volleyball Detection & Tracking</h3></summary>

<a href="https://universe.roboflow.com/shukur-sabzaliev-bh7pq/volleyball-tracking/model/">
    <img src="https://app.roboflow.com/images/try-model-badge.svg"></img>
</a>
<a href="https://universe.roboflow.com/shukur-sabzaliev-bh7pq/volleyball-tracking">
    <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
</a>
<a href="https://github.com/shukkkur/VolleyVision/tree/main/Stage%20I%20-%20Volleyball/weights/weights"><img src="https://img.shields.io/badge/Download-YOLOV7--TINY%20Weights-red" alt="yV8 Weights"></a>
<a href="https://wandb.ai/volleyvision/YOLOR/runs/2u30vyzp/overview?workspace=user-shukkkur"><img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-gradient.svg" alt="WandB Badge"></a>

<!--   <strong>February 10, 2023 </strong> -->
<!--    <i>Closing the first stage moderetly satisfied</i>.  -->
<!--   <br> -->

<p>Two trained models: <a href="https://blog.roboflow.com/new-and-improved-roboflow-train/">RoboFlow</a> (<a href="https://docs.roboflow.com/train">AutoML training</a>) and <a href="https://github.com/WongKinYiu/yolov7">yoloV7-tiny</a> (local training). Both were trained on my newly created <a href="https://universe.roboflow.com/volleyvision/volleyball-tracking/dataset/13">dataset</a> comprised of <strong>25k</strong> images.  As for the tracker, <a href="https://github.com/foolwood/DaSiamRPN">DaSiamRPN</a> (<a href="https://docs.opencv.org/4.x/de/d93/classcv_1_1TrackerDaSiamRPN.html">cv2</a>) was used.
  
|              | yoloV7-tiny | RoboFlow |
|:------------:|:----------:|:---------:|
|**mAP**       |    74.1%    |   92.3%  |
|**precision** |    86.4%    |   94.7%  |
|**recall**    |    65.8%    |   86.1%  |

  <strong>RoboFlow</strong> model is more accurate and works better on official matches, rather than yolov7 model. However, it requires longer time for inference. <strong>YoloV7-tiny</strong> is capable of real-time inference, even though it is less accurate than RoboFlow model, it is still a good and fast choice for larger volleyballs.</p>
</details>

<details><summary><h3>Stage II | Action Recognition & Player Detection</h3></summary>
    <h4>Action Recognition</h4>
    <a href="https://universe.roboflow.com/shukur-sabzaliev-42xvj/volleyball-actions"><img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img></a>
    <a href="https://universe.roboflow.com/shukur-sabzaliev-42xvj/volleyball-actions/model/"><img src="https://app.roboflow.com/images/try-model-badge.svg"></img></a>
    <a href="https://github.com/shukkkur/VolleyVision/tree/main/Stage%20II%20-%20Players%20%26%20Actions/weights/actions/yV8_medium/weights"><img src="https://img.shields.io/badge/Download-YOLOV8M%20Weights-red" alt="yV8 Weights"></a>
    <a href="https://wandb.ai/volleyvision/YOLOv8/runs/28bs84bi/overview?workspace=user-shukkkur"><img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-gradient.svg" alt="WandB Badge"></a>
    <p>
      In progress...
    </p>  
    <h4>Players Detection</h4>
    <a href="https://universe.roboflow.com/shukur-sabzaliev-42xvj/players-dataset"><img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img></a>
    <a href="https://universe.roboflow.com/shukur-sabzaliev-42xvj/players-dataset/model/"><img src="https://app.roboflow.com/images/try-model-badge.svg"></img></a>
    <a href="https://github.com/shukkkur/VolleyVision/tree/main/Stage%20II%20-%20Players%20%26%20Actions/weights/players/yV8_large/weights"><img src="https://img.shields.io/badge/Download-YOLOV8L%20Weights-red" alt="yV8 Weights"></a>
     <a href="https://github.com/shukkkur/VolleyVision/tree/main/Stage%20II%20-%20Players%20%26%20Actions/weights/players/yV8_medium"><img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-gradient.svg" alt="WandB Badge"></a>
    <p>
      In progress...
    </p>  
</details>


<details><summary><h3>Stage III | Court Tracking</h3></summary>
<p>
  Someday ... 
</p>
</details>

<h2>💾 Datasets</h2>

| Volleyball | Actions | Players | Court |
|------|---------|---------|-------|
| <a href="https://universe.roboflow.com/shukur-sabzaliev-bh7pq/volleyball-tracking"><img src="https://github.com/shukkkur/VolleyVision/blob/6ac8230e48de95a8edb3a1c4793657ddb06f1409/README_files/volley-collage.jpg" width="600"></a> | <a href="https://universe.roboflow.com/shukur-sabzaliev-42xvj/volleyball-actions"><img src="https://github.com/shukkkur/VolleyVision/blob/f59e9feba6946d6ce7706b8c6b27081461d0401e/assets/actions_collage.png" width="600"></a> | <a href="https://universe.roboflow.com/shukur-sabzaliev-42xvj/players-dataset"><img src="https://github.com/shukkkur/VolleyVision/blob/f59e9feba6946d6ce7706b8c6b27081461d0401e/assets/players_collage.png" width="600"></a> | <img src="https://github.com/shukkkur/VolleyVision/blob/280fed79d290c1cf6d53c869fa60355eeb04d148/assets/in_progress.jpg" width="600"> |



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
  
<details><summary><h2>📝 LICENSE</h2></summary>
<p>This project is licensed under the <strong>Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND)</strong> license.</p>
<p>This license allows you to:</p>
<ul>
    <li><strong>Share</strong> — copy and redistribute the material in any medium or format</li>
    <li><strong>Adapt</strong> — remix, transform, and build upon the material</li>
</ul>
<p>Under the following terms:</p>
<ul>
    <li><strong>Attribution</strong> — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.</li>
    <li><strong>Non-Commercial</strong> — You may not use the material for commercial purposes.</li>
    <li><strong>No Derivatives</strong> — If you remix, transform, or build upon the material, you may not distribute the modified material.</li>
</ul>
<p>See the full license text for more details.</p>
<p>
<a href="https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode">Read the full license text</a>
</p>
</details>

<details><summary><h2>💖 Sponsor</h2></summary>
<p>If you find my work useful or interesting, please consider supporting me on <strong><a href="https://ko-fi.com/shukkkur">Ko-fi</a></strong>.</p>
</details>

<details><summary><h2>🙌 Acknowledgement</h2></summary>
  <ul>
    <li>
    This project wouldn't possible without amazing & free RoboFlow <a href="https://roboflow.com/annotate">annotation tools</a> , open-source <a href="https://universe.roboflow.com/">datasets</a>, quick & easy <a href="https://roboflow.com/deploy">deployement</a> and high-level <a href="https://blog.roboflow.com/">blog posts</a></li>
  <li>Supervisor</li>
  <li>Course Instructor</li>
  <li>University of Central Asia</li>
  </ul>
</details>

<details><summary><h2>📞 Contact</h2></summary>

<p>
<i><strong>For any additional quesitons feel free to <a href="https://github.com/shukkkur/VolleyVision/issues/new">open an issue</a> or <a href="https://github.com/shukkkur#feel-free-to-connectcontact">contact me</a></strong></i>
</p>
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

<!-- <img src="https://github.com/shukkkur/VolleyVision/blob/2e4ce97819f591573de99fcfe04ba0f0259dff9a/assets/rf_men_rally.gif" width="350" height="250"> | <img src="https://github.com/shukkkur/VolleyVision/blob/2e4ce97819f591573de99fcfe04ba0f0259dff9a/assets/rf_women_rally.gif" width="350" height="250"> -->

<!--   https://blog.roboflow.com/new-and-improved-roboflow-train/ -->

<!-- I was trying to train the standard <a href="https://github.com/WongKinYiu/yolov7#performance">yolov7</a>, however, with GPU memory being 4GB, I could only afford training with <code>batch_size=8 img-size=480</code>, which didn't yield best results. -->
