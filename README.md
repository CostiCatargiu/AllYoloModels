# AllYoloModels
## Short Introduction
Hello everyone! 😊

My name is Catargiu Constantin and I am studying PhD at Gheorghe Asachi University in Iasi, Romania. During my work research I've started to read and learn about YOLO(You Only Look Once) models which can be used for Object Detection, Object  Tracking, Image Classification and Image Segmentation and also to use them in some object detection applications. Because there are many versions of the YOLO model (currently the latest one is YoloV9) is somehow hard to decide which one fits best for a certaion application, so I've tested each model starting with version 5 to version 9. Testing means that I performed:

  - 📊 Evaluation on Test and Valid data.
  
  - 🏋️‍♂️ Training on custom dataset.
  
  - 🧠 Inference on videos files and images.

During my experiments, I gained experience with the scripts provided in the orignal repositorys by the authors of the models, and I want to share this with you. Due to the fact that the models are developed by different scientists, their  usage differ and in this repo I made same .sh file in which facilitate the usage of train, evaluation and inference scripts in just one line of code for every model that you want to use 😊

## Features

- ⬇️ Clone/Reclone and prepare the setup for which model you want in just a line of code using **DownloadModel.sh**.
- 🔧 **YoloModelsEval.sh**, **YoloModelsInference.sh** and **YoloModelsTrain.sh** offer the possibility to perform training, inference, or evaluation tasks in just a line of code using a selected model.
- 📈  Experimental results that were obtained during my experiments using all the models mentioned here.

<details>
  <summary>Project overview</summary>
After this repository is cloned the structure of the project will look like in the images bellow with the mention that the **YoloModels** directory is empty because no model is cloned there.

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/76f8e45a-f182-48ff-860e-bf4094b66c2b) ![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/4aab8c84-1748-40bc-a399-fdecd570a6eb)

</details>

## Quick start

<details>
    <summary>Give permission for .sh scripts on Linux</summary>

  ```bash
  chmod +X DownloadModel.sh
  chmod +X YoloModelsEval.sh
  chmod +X YoloModelsInference.sh
  chmod +X YoloModelsTrain.sh

  ```

</details>

<details>
  <summary>Clone specific YOLO model</summary>
  
  To clone a specifi yolo model $\color{magenta}{\textsf{DownloadModel.sh}}$ is used that requires on parameter from the list  $\color{orange}{\textsf{(yolov5, yolov6, yolov7, yolov8, yolov9)}}$.
  
  ```bash
  ./DownloadModel.sh yolov5
  ```

Notice that first you clone the model, $\color{magenta}{\textsf{requirements.txt}}$ for it will be also installed.
After the model is cloned it will appear in $\color{magenta}{\textsf{YoloModels}}$ directory. If the model is already there and the script is executed and message will appear and ask if we want to reclone or no.

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/ac73a342-45ef-4668-a298-0d481387bc18)

</details>

<details>
  <summary>Dowmload COCO dataset</summary>

To download COCO dataset you can use $\color{red}{\textsf{Utility/DatasetDownloadScripts/getcoco.sh}}$ .

The dataset will be downloaded in $\color{red}{\textsf{Utility/COCOdatasets}}$.

Please note that the labels for the testing set are not available, or at least I didn't find them. Another observation is that for YoloV6, we need to use bounding box format labels instead of polygon format labels for the evaluation task.

In the **get_coco.sh** script, we can select between downloading the train, test, valid, and segment data. By default, all datasets will be downloaded.

The YAML file for COCO dataset is located at path $\color{red}{\textsf{Utility/YAMLconfigs/coco.yaml}}$

Dataset size is around 27GB ( 5000 valid images, 40 670 test images and 118 287 train images)
</details>

## Evaluation task

 $\color{red}{\textsf{YoloModelsEval.sh}}$ file shall be used for this task. This file will trigger the inference script for the selected model.

Syntax:

./YoloModelsEval.sh  <<select_model>> --[datasetPath] val --[weights] val --[batchSize] val --[conf_thr] val --[img_size] val --[testSplit] "val"

Usage example:
  ```bash
 ./YoloModelsEval.sh yolov5m #use default parameters
```
Parameters: 
 << >> = required parameter; [ ]=optional parameter
 --testSplit parameter allows us to select between "train" and "valid" dataset for evaluate the model.
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/8e21d24a-c73b-4d63-ad9f-265fa56b8686)

If you want to add more parameters to evaluation task please edit the .sh for the desired model.

<table border="1">
  <tr>
    <th></th>
    <th align="center">$\color{red}{\textsf{YoloV5l}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV6l}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV7}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV8l}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV9-e}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV9-gelan-e}}$</th>

  </tr>
  <tr>
    <td>$\color{orange}{\textsf{maP@0.50}}$</td>
    <td align="center">0.69</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>

  </tr>
    <tr>
    <td>$\color{orange}{\textsf{maP@0.50-95}}$</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>
    
  </tr>
  
  <tr>
    <td>$\color{orange}{\textsf{confThr}}$</td>
    <td align="center">0.001</td>
    <td align="center">0.001</td>
    <td align="center">0.001</td>
    <td align="center">0.001</td>
    <td align="center">0.001</td>
    <td align="center">0.001</td>

  </tr>
  <tr>
    <td>$\color{orange}{\textsf{iouThr}}$</td>
    <td align="center">65</td>
    <td align="center">65</td>
    <td align="center">65</td>
    <td align="center">65</td>
    <td align="center">65</td>
    <td align="center">65</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{bathSize}}$</td>
    <td align="center">32</td>
    <td align="center">32</td>
    <td align="center">32</td>
    <td align="center">32</td>
    <td align="center">32</td>
    <td align="center">32</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{speed(ms/img)}}$</td>
    <td align="center">3.5</td>
    <td align="center">3.5</td>
    <td align="center">3.5</td>
    <td align="center">3.5</td>
    <td align="center">3.5</td>
    <td align="center">3.5</td>

  </tr>
  <tr>
    <td>$\color{orange}{\textsf{GPU}}$</td>
    <td colspan="7" align="center" >$\color{green}{\textsf{NVIDIA GeForce RTX 4090, 24209MiB}}$</td>
  </tr>
  
</table>


<details>
  <summary>Evaluation on COCO dataset using yolov5l </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/3993b392-1120-480a-ade3-823087e5e1e1)


</details>

<details>
  <summary>Evaluation on COCO dataset using yolov6l </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/b001d8d6-bff8-4a23-bb70-bebd7420bd96)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/46c44ab4-03b2-4313-bbc9-44ec6ba20c53)

</details>


<details>
  <summary>Evaluation on COCO dataset using yolov7 </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/5eb42bbf-2647-4fa3-b9b6-e17b928d34ea)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/6bb8fad1-93e3-4947-9d28-c86f3bfeced8)

</details>

<details>
  <summary>Evaluation on COCO dataset using yolov8l </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/069538f6-fa61-462f-bcb9-f95a871dca38)

</details>

<details>
  <summary>Evaluation on COCO dataset using yolov9-e </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/cb58d821-0462-4c93-93f6-e110cdf0582e)

</details>

<details>
  <summary>Evaluation on COCO dataset using yolov9_gelan-e </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/451f47b8-ca6a-40b8-ac9b-5e5ef451738f)

</details>


