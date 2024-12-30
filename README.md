# AllYoloModels

![oooutput_filename](https://github.com/user-attachments/assets/ffa75120-a17f-4f5c-849d-5fc5959e155a)

![ooutput_filename](https://github.com/user-attachments/assets/d27af7bd-a97e-44b6-bde4-6f0e287950e5)


## Short Introduction
Hello everyone! 😊

My name is Catargiu Constantin and I am studying PhD at Gheorghe Asachi University in Iasi, Romania. During my work research I've started to read and learn about YOLO(You Only Look Once) models which can be used for Object Detection, Object  Tracking, Image Classification and Image Segmentation and also to use them in some object detection applications. Because there are many versions of the YOLO model (currently the latest one is Yolo11) is somehow hard to decide which one fits best for a certaion application, so I've tested each model  $\color{red}{\textsf{(YoloV5, YoloV6, YoloV7, YoloV8, YoloV9, YoloV10, YoloV11 and YoloNAS)}}$. Testing means that I performed:

  - 📊 Evaluation on Test and Valid data.
  
  - 🏋️‍♂️ Training on custom dataset.
  
  - 🧠 Inference on videos files and images.

During my experiments, I gained experience with the scripts provided in the orignal repositorys by the authors of the models, and I want to share this with you. Due to the fact that the models are developed by different scientists, their  usage differ and in this repo I made same .sh file in which facilitate the usage of train, evaluation and inference scripts in just one line of code for every model that you want to use 😊

## Features

- ⬇️ Clone/Reclone and prepare the setup for which model you want in just a line of code using $\color{yellow}{\textsf{DownloadModel.sh}}$.
- 🔧 $\color{green}{\textsf{YoloModelsEval.sh}}$, $\color{orange}{\textsf{YoloModelsInference.sh}}$ and $\color{magenta}{\textsf{YoloModelsTrain.sh}}$ offer the possibility to perform training, inference, or evaluation tasks in just a line of code using a selected model.
- 📤 $\color{red}{\textsf{YoloModelsExport.sh}}$ help us to export a specific model to ONNX or TensorRT.
- 📈 The experimental results from my work with all the models discussed here are stored on Google Drive, with some of them also shared here.
<details>
- 🔍 I created a script which run after each Inference task, to analyze models by evaluating detection counts and average confidence per class, enabling performance comparison.

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
  chmod +X YoloModelsExport.sh

  ```

</details>

<details>
  <summary>Clone specific YOLO model</summary>
  
  To clone a specifi yolo model $\color{magenta}{\textsf{DownloadModel.sh}}$ is used that requires on parameter from the list  $\color{orange}{\textsf{(yolov5, yolov6, yolov7, yolov8, yolov9, yolov10, yolo11)}}$.
  
  ```bash
  ./DownloadModel.sh yolov5
  ```

Notice that first you clone the model, $\color{magenta}{\textsf{requirements.txt}}$ for it will be also installed.
After the model is cloned it will appear in $\color{magenta}{\textsf{YoloModels}}$ directory. If the model is already there and the script is executed a message will appear and ask if we want to reclone or no.

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/ac73a342-45ef-4668-a298-0d481387bc18)

</details>


## Evaluation task

 $\color{red}{\textsf{YoloModelsEval.sh}}$ file shall be used for this task. This file will trigger the evaluation script for the selected model.

Syntax:

$\color{yellow}{\textsf{./YoloModelsEval.sh}}$ <<select_model>> --[datasetPath] val --[weights] val --[batchSize] val --[conf_thr] val --[img_size] val --[testSplit] "val"

Usage example:
  ```bash
 ./YoloModelsEval.sh yolov5m #use default parameters
 ./YoloModelsEval.sh yolo11l --batchSize 64 --cnfThr 0.1 --iouThr 0.7 --testSplit valid #custom parameters

```
$\color{orange}{\textsf{Parameters:}}$ 
 << >> = required parameter; [ ]=optional parameter

 ![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/2cf3f3c5-df09-402a-9194-ace8c400eb05)

 -- $\color{orange}{\textsf{testSplit}}$ parameter allows us to select between "train" and "valid" dataset for evaluate the model.

If you want to add more parameters to evaluation task please edit $\color{red}{\textsf{YoloModelsEval.sh}}$ for the desired model. In the table above are presented the results obtained after evaluting the models on COCO2017 dataset.  

<table border="1">
  <tr>
    <th></th>
    <th align="center">$\color{red}{\textsf{YoloV5l}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV6l}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV7}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV8l}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV9-e}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV9-gelan-e}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV10l}}$</th>
    <th align="center">$\color{red}{\textsf{Yolo11l}}$</th>
    
  </tr>
  <tr>
    <td>$\color{orange}{\textsf{maP@0.50}}$</td>
    <td align="center">0.69</td>
    <td align="center">0.69</td>
    <td align="center">0.69</td>
    <td align="center">0.71</td>
    <td align="center">0.73</td>
    <td align="center">0.72</td>
    <td align="center">0.70</td>
    <td align="center">0.68</td>

  </tr>
    <tr>
    <td>$\color{orange}{\textsf{maP@0.50-95}}$</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>
    <td align="center">0.50</td>
    <td align="center">0.57</td>
    <td align="center">0.56</td>
    <td align="center">0.55</td>
    <td align="center">0.54</td>
    <td align="center">0.53</td>
    
  </tr>
  
  <tr>
    <td>$\color{orange}{\textsf{confThr}}$</td>
    <td align="center">0.001</td>
    <td align="center">0.001</td>
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
    <td align="center">65</td>
    <td align="center">65</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{batchSize}}$</td>
    <td align="center">32</td>
    <td align="center">32</td>
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
    <td align="center">4</td>
    <td align="center">4.4</td>
    <td align="center">4</td>
    <td align="center">9.2</td>
    <td align="center">8</td>
    <td align="center">3.5</td>
    <td align="center">2.8</td>

  </tr>
  <tr>
    <td>$\color{orange}{\textsf{GPU}}$</td>
    <td colspan="7" align="center" >$\color{green}{\textsf{NVIDIA GeForce RTX 4090, 24209MiB}}$</td>
  </tr>
  
</table>

<details>
  <summary>📥 $\color{magenta}{\textsf{Dowmload COCO dataset}}$ 📥</summary>

To download COCO dataset you can use $\color{red}{\textsf{Utility/DatasetDownloadScripts/getcoco.sh}}$ .

The dataset will be downloaded in $\color{red}{\textsf{Utility/COCOdatasets}}$.

Please note that the labels for the testing set are not available, or at least I didn't find them. Another observation is that for YoloV6, we need to use bounding box format labels instead of polygon format labels for the evaluation task.

In the **get_coco.sh** script, we can select between downloading the train, test, valid, and segment data. By default, all datasets will be downloaded.

The YAML file for COCO dataset is located at path $\color{red}{\textsf{Utility/YAMLconfigs/coco.yaml}}$

Dataset size is around 27GB ( 5000 valid images, 40 670 test images and 118 287 train images)

![image](https://github.com/user-attachments/assets/94abb611-7d2e-435f-8930-3674077297f3)

</details>

<details>
  <summary>⬇️ $\color{magenta}{\textsf{To see more detailed results obtained on evaluation task please see above.}}$ ⬇️</summary>


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

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/b73ccf56-b06d-484b-ab70-ec0ea560dfaf)

</details>


<details>
  <summary>Evaluation on COCO dataset using yolov8l </summary>
  
  ![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/df790ffa-62d5-4ccf-a07d-6943d733b5f7)

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

<details>
  <summary>Evaluation on COCO dataset using yolov10l </summary>

![image](https://github.com/user-attachments/assets/aa676a38-2113-4046-b250-40226026366b)

</details>


<details>
  <summary>Evaluation on COCO dataset using yolo11l </summary>

![image](https://github.com/user-attachments/assets/2a830aa2-9dd7-46ea-a505-d387d1ec7629)

</details>

</details>

## Export task

The $\color{yellow}{\textsf{YoloModelsExport.sh}}$ script is designated for this task, responsible for generating ONNX or ENGINE files for the desired model. Notably, this script is automatically triggered whenever $\color{yellow}{\textsf{YoloModelsInference.sh}}$ is executed.

![image](https://github.com/user-attachments/assets/fe84e075-35d8-4195-984f-ab252d124932)

![image](https://github.com/user-attachments/assets/ae21b27b-20c1-492c-9be1-8d9c6c09a686)

Usage example:
  ```bash
#convert pretrained yolo11m model version to ENGINE type
./YoloModelsExport.sh yolo11m --exportType engine

#convert pretrained yolo11x model version to ONNX type
./YoloModelsExport.sh yolo11x --exportType onnx

```
## Inference task

 $\color{yellow}{\textsf{YoloModelsInference.sh}}$ file shall be used for this task. This file will trigger the inference script for the selected model.

Syntax:

$\color{orange}{\textsf{./YoloModelsInference.sh}}$   <<select_model>> --[weights] val --[source_video] val --[conf_thr] val --[device] "val" --[count] "class1,class2..." -[filter] "class1,class2..." and other parameters can be added; they are listed and explained in the content bellow.

Usage example:
  ```bash
#infer with the default parameters defined in .sh file
 ./YoloModelsInference.sh yolov8s

 #count the number of detections for classes in " " which a confidence threshold of 0.5
 ./YoloModelsInference.sh yolov5l --count "car,person,bicycle,truck"  --conf_thr 0.5

#filter one class to not be displayed the detections for it egg. "car" class
 ./YoloModelsInference.sh yolov9-c --count "person,bicycle,truck" --filter "car"  --conf_thr 0.5

#in this command line the fontSize, fontThickness and the position on y_axes are configured for a better appearence in the image of the
#additional data which is diplayed 
./YoloModelsInference.sh yolov9-c --conf_thr 0.6 --count "person,car" --filter "bus" --fontSize 1 --fontThickness 3 --ypos 50
or
./YoloModelsInference.sh yolov9-c -p3 0.6 -p5 "person,car" -p6 "bus" -p7 1 -p8 3 -p9 50

#in this command lines we can choose between engine and pytorch weights to use for inference
./YoloModelsInference.sh yolo11x --video_index 1 --fontSize 1.2 --fontThickness 2 --ypos 34 --initialypos 20 --labelTextSize 2 --weightsType engine  --count "car,person"
./YoloModelsInference.sh yolov10b --video_index 2 --fontSize 1.2 --fontThickness 3 --ypos 36 --initialypos 20 --labelTextSize 4 --weightsType pytorch  --count "bus,truck,train"

```
Parameters: 

 << >> = required parameter; [ ]=optional parameter
 
![image](https://github.com/user-attachments/assets/64e4ed3a-af57-40d6-ae22-299ec122eedc)

If you want to add more parameters to inference task please edit the $\color{red}{\textsf{YoloModelsInference.sh}}$ for the desired model.


<details>
  <summary>$\color{magenta}{\textsf{Short explanation of parameters usage}}$</summary>
  

The image above shows a variety of parameters available for selection, depending on what we aim to achieve in the inference task.
1. $\color{orange}{\textsf{model}}$: the only mandatory parameter required to initiate the inference process. It specifies the version of the YOLO model to be used for the inference task. The available options for this parameter are shown in the image above. All subsequent parameters are optional, and default values will be used if they are not provided.
   
2. $\color{orange}{\textsf{-p1 || --weights}}$: This parameter specifies the path to the weights that wiil be used for the inference. Default value for this:  $\color{gray}{\textsf{/ExperimentalResults/YoloV.../weights/<model>.pt}}$.

3. $\color{orange}{\textsf{p2 || --source video}}$: This parameter specifies the path to the video that will be used for inference. To simplify the selection of the desired video for inference, all files have been placed in a specific directory. From there, one can choose a video by indicating its index in the list (the image above displays all my test videos along with their respective indexes). The index of the video is specified using the next parameter.

4. $\color{orange}{\textsf{-p3 || --video index}}$: This parameter is used to indicate the list index of the video that will be used for inference.

5. $\color{orange}{\textsf{-p4 || --conf thr}}$: This parameter is used to set the cofindence threshold for the detection. Will be processed only the predictions with a precision greater than this threshold.

6. $\color{orange}{\textsf{-p5 || --device}}$: This parameter indicates the devide which will be used for the inference. We can choose 0 for GPU or "cpu".

7. $\color{orange}{\textsf{-p6 || --count}}$: This parameter is essentially a list where you can specify certain classes that the model was trained on. Using this parameter allows you to count and display the number of detections for the specified classes in each frame. By default this option is disabled.

8. $\color{orange}{\textsf{-p7 || --filter}}$: This parameter is essentially a list where you can specify certain classes that the model was trained on. Using this parameter allows you to exclude the specified classes from being displayed in the inference output. By default, this option is disabled.

9. $\color{orange}{\textsf{-p8 || --fontSize}}$: This parameter allows you to configure the text dimensions of the information displayed during video inference. This is useful because video resolutions can vary, and the text may be too small or too large depending on the resolution.

10. $\color{orange}{\textsf{-p9 || --fontThickness}}$: Similar to the previous parameter.

11.  $\color{orange}{\textsf{-p10 || --ypos}}$: This parameter is related to -p8 and -p9 and allows you to modify the distance between lines of displayed information to better fit within the image.

12. $\color{orange}{\textsf{-p11 || --initialypos}}$: Initial position of text on y axis.

13. $\color{orange}{\textsf{-p12 || --labelTextColor}}$: This parameter allows you to change the label text color, which can be useful when the text color is hard to distinguish from the background.

14. $\color{orange}{\textsf{-p13 || --labelTextSize}}$: This parameter allows you to adjust the label text size, which can be useful for different video resolutions where the text on certain labels may not be clearly visible.

15. $\color{orange}{\textsf{-p14 || --nrCompareFrames}}$: This parameter set the number of consecutive frames that will be compared to see if we had false positive or wrong predictions.

16. $\color{orange}{\textsf{-p15 || --saveConfusedPred}}$: This parameter allow us to save the frames in wich we had wrong predictons, that can help to make a short analysis and see were the model is not so good.

17. $\color{orange}{\textsf{-p16 || --boxSimilarity}}$: This parameter dynamically defines the pixel threshold to determine whether two detections are considered mismatched.

18. $\color{orange}{\textsf{-p17 || --weightsType}}$: This parameter allows us to choose between Pytorch weights type or Engine weights type.

19. $\color{orange}{\textsf{-p18 || --display info}}$: This parameter allows us to display or not the text during Inference task

20. $\color{orange}{\textsf{-p19 || --thr metric}}$: This parameter sets a threshold for the metrics calculated after the inference process, based on the number of predictions per class and their confidence levels. Upon completion of the inference, a txt file with two tables will be generated: one displaying the number of predictions and their average precision for each class with a confidence greater than this threshold, and a second table with the same information for predictions with a confidence below this threshold.
</details>

$\color{darkorange}{\textsf{Advantages of this implementation:}}$

<details>
  <summary> -💻 During inference, details such as the device used, model, number of frames, FPS, and inference time are displayed on the output video. These details help monitor and assess the performance of the inference process. Additionally, there are customization options available to better fit the data on the video, such as adjusting the text size, thickness, and vertical positioning. </summary>

  ```bash
./YoloModelsInference.sh yolov8m --conf_thr 0.45 --count "car,person,bus,bicycle"  --labelTextColor "white" --fontSize 2 --fontThickness 2 --ypos 60 --video_index 15 --labelTextSize 2  --thr_metric 0.6
  ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/ba75d996-1c6e-41bd-80de-42c3d3b9e0fd)

</details>


<details>
  <summary> - 👁️‍🗨️ We can monitor the number of appearances of a certain object class across the frames. </summary>
  
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/a8d2612f-b584-48ff-8bc7-fb2da7ff501a)

</details>

  <details>
  <summary> - 🚫 We can filter the detection of a certain class if it is not of interest to us. </summary>
    
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/22e8d381-8147-442e-a5b2-d47521270cc2)

</details>
  <details>
  <summary> - 🚀 Switching between PyTorch and Engine weights made  very easy modifying a single parameter ( --weightsType)  </summary>
    
I created the $\color{orange}{\textsf{YoloModelsExport.sh}}$ script, which is automatically invoked by $\color{orange}{\textsf{YoloModelsInference.sh}}$ if the Engine file for the specified model has not been generated yet. This script streamlines the process of exporting the model's weights and facilitates seamless switching between PyTorch and Engine file types.

![image](https://github.com/user-attachments/assets/47edfb30-edc6-40fb-b33b-8946c26d1aa5)

  ```bash
#engine weights
./YoloModelsInference.sh yolov5m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType engine  --count "car,person,bicycle,bus,traffic light" 
 ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/920384ff-3cab-4384-8bc7-3b82b62e5ec5)

  ```bash
#pytorch weights
./YoloModelsInference.sh yolov5m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType pytorch  --count "car,person,bicycle,bus,traffic light" 
 ```

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/90b160c8-b631-48f5-935a-06eb5afaae64)

</details>

  <details>
  <summary> - 💡 We can monitor if the model is making incorrect predictions by checking if it assigns different class labels to the same object . . </summary>

Parameters:
 --nrCompareFrames=4 (default) 
 --boxSimilarity=5 (default)
 
In this example the model is making a missmatch between bycile and motorcycle.
  
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/017ecffd-888c-417f-9743-0a8688b149b3)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/b41465e0-1e6b-4bbc-b100-062bb1176943)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/0c62f06b-3c2f-423e-be55-1d6e4d828640)

In this example the model is making a missmatch between bus and airplane.

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/5422b26b-0cf1-4450-8f7a-0c1be28dca6f)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/cb197e93-bbec-49d0-a0b6-28e15f06b53f)

</details>
  <details>
  <summary>  - 📈 After the inference ends, some useful metrics will be outputted indicating the performance of the model. These metrics include: </summary>
    
    a. The total number of objects detected for all classes in the video.

    b. The total number of detections for each class over the frames.
        
    c. The average precision for each class over the frames.
    
    d. The average FramesPerSecond (FPS).

    e. The time for inference process.
These metrics are saved in TXT format and are automatically stored after each inference task at the following path: egg. $\color{darkorange}{\textsf{ExperimentalRresults/YoloV9/inferGelan/exp28/gelan-c.txt}}$

  <details>
  <summary> gelan-m.txt </summary>
    
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/0dab65ca-873a-490c-9e65-b273d0ea7b97)
  </details>
  
  <details>
  <summary> yolov8m.txt </summary>
    
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/f87050e1-6e49-4376-abe2-aa3a1aecdf16)

    
  </details>

  <details>
  <summary>yolov10b.txt </summary>
    
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/c5bc660a-034c-48b6-af20-bc4e178e9eb0)
  </details>


Additionally, there's an option to create a separate TXT file that compares the results obtained from each model after inference.The key advantage of this new TXT file is that it structures the data into tables, enabling straightforward and efficient comparison of performance across different models. This tabular arrangement simplifies the analysis, allowing users to quickly assess and contrast the effectiveness of each model based on two metrics: average precision per class and total number of detection per class. This organized format is especially beneficial for identifying the most suitable model for specific tasks or environments.

To generate this new metric we need to follow 2 steps:
1. Put the .txt files that you want to compare at the following path: $\color{darkorange}{\textsf{ExperimentalResults/Metrics/}}$
2. Execute the .py script:  $\color{darkorange}{\textsf{Utils/Scripts/generatemetric.py}}$. The script will generate a $\color{darkorange}{\textsf{Utils/Scripts/metric.txt}}$ file that contains the compared data for the models selected. 

ENGINE weights

![image](https://github.com/user-attachments/assets/8e13dadb-d0ac-489a-9323-62dc48e136e1)

![image](https://github.com/user-attachments/assets/dc53173d-e6ef-43d4-9a9a-3f9ee2341ad7)

PYTORCH weights

![image](https://github.com/user-attachments/assets/356cd440-5ca3-4f06-a295-6cb357d6332d)

![image](https://github.com/user-attachments/assets/6eb62e7b-0fbf-4ee6-a632-618b2e04897a)

</details>


</details>

  <details>
  <summary> 😊 Please check also the detailed inference results that are presented bellow 🔍 </summary>

<details>
  <summary> Compariston between results obtained after inference on video using all 6 models </summary>

<table border="1">
  <tr>
    <th></th>
    <th align="center">$\color{red}{\textsf{classes}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV5l}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV6l}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV7}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV8l}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV9-c}}$</th>
    <th align="center">$\color{red}{\textsf{YoloV9-gelan-c}}$</th>
  </tr>

  <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{person}}$</td>
    <td align="center">9779</td>
    <td align="center">10385</td>
    <td align="center">10962</td>
    <td align="center">9924</td>
    <td align="center">10009</td>
    <td align="center">13342</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{person}}$</td>
    <td align="center">0.55</td>
    <td align="center">0.67</td>
    <td align="center">0.57</td>
    <td align="center">0.68</td>
    <td align="center">0.58</td>
    <td align="center">0.59</td>
  </tr>
  <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{bicycle}}$</td>
    <td align="center">1909</td>
    <td align="center">1656</td>
    <td align="center">1984</td>
    <td align="center">1567</td>
    <td align="center">1361</td>
    <td align="center">2644</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{bicycle}}$</td>
    <td align="center">0.60</td>
    <td align="center">0.83</td>
    <td align="center">0.65</td>
    <td align="center">0.54</td>
    <td align="center">0.65</td>
    <td align="center">0.68</td>
  </tr>
  <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{car}}$</td>
    <td align="center">16668</td>
    <td align="center">14124</td>
    <td align="center">13396</td>
    <td align="center">13482</td>
    <td align="center">13514</td>
    <td align="center">15156</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{car}}$</td>
    <td align="center">0.71</td>
    <td align="center">0.70</td>
    <td align="center">0.76</td>
    <td align="center">0.75</td>
    <td align="center">0.74</td>
    <td align="center">0.76</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{truck}}$</td>
    <td align="center">2586</td>
    <td align="center">4664</td>
    <td align="center">5880</td>
    <td align="center">4167</td>
    <td align="center">4710</td>
    <td align="center">6391</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{truck}}$</td>
    <td align="center">0.88</td>
    <td align="center">0.75</td>
    <td align="center">0.89</td>
    <td align="center">0.73</td>
    <td align="center">0.86</td>
    <td align="center">0.86</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{bus}}$</td>
    <td align="center">2008</td>
    <td align="center">2175</td>
    <td align="center">1534</td>
    <td align="center">1919</td>
    <td align="center">1712</td>
    <td align="center">1660</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{bus}}$</td>
    <td align="center">0.85</td>
    <td align="center">0.83</td>
    <td align="center">0.86</td>
    <td align="center">0.79</td>
    <td align="center">0.83</td>
    <td align="center">0.83</td>
  </tr>
      <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{traffic light}}$</td>
    <td align="center">1272</td>
    <td align="center">861</td>
    <td align="center">1456</td>
    <td align="center">918</td>
    <td align="center">1007</td>
    <td align="center">3278</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{traffic light}}$</td>
    <td align="center">0.90</td>
    <td align="center">0.78</td>
    <td align="center">0.92</td>
    <td align="center">0.61</td>
    <td align="center">0.89</td>
    <td align="center">0.90</td>
  </tr>
      <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{motorcycle}}$</td>
    <td align="center">703</td>
    <td align="center">194</td>
    <td align="center">334</td>
    <td align="center">349</td>
    <td align="center">84</td>
    <td align="center">1640</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{motorcycle}}$</td>
    <td align="center">0.83</td>
    <td align="center">0.7</td>
    <td align="center">0.86</td>
    <td align="center">0.56</td>
    <td align="center">0.79</td>
    <td align="center">0.82</td>
  </tr>
      <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{backpack}}$</td>
    <td align="center">134</td>
    <td align="center">0</td>
    <td align="center">8</td>
    <td align="center">7</td>
    <td align="center">1</td>
    <td align="center">139</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{backpack}}$</td>
    <td align="center">0.90</td>
    <td align="center">0.00</td>
    <td align="center">0.93</td>
    <td align="center">0.54</td>
    <td align="center">0.91</td>
    <td align="center">0.91</td>
  </tr>
        <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{stop sign}}$</td>
    <td align="center">274</td>
    <td align="center">74</td>
    <td align="center">16</td>
    <td align="center">0</td>
    <td align="center">0.72</td>
    <td align="center">112</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{stops sign}}$</td>
    <td align="center">0.89</td>
    <td align="center">0.7</td>
    <td align="center">0.91</td>
    <td align="center">0.00</td>
    <td align="center">0.72</td>
    <td align="center">0.91</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{suitcase}}$</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">41</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{suitcase}}$</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.92</td>
  </tr>
      <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{potted plant}}$</td>
    <td align="center">14</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">6</td>
    <td align="center">0.72</td>
    <td align="center">1</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{potted plant}}$</td>
    <td align="center">0.89</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.54</td>
    <td align="center">0.00</td>
    <td align="center">0.92</td>
  </tr>
        <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{bird}}$</td>
    <td align="center">3</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">11</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{bird}}$</td>
    <td align="center">0.89</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.92</td>
  </tr>
        <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{handbag}}$</td>
    <td align="center">2</td>
    <td align="center">39</td>
    <td align="center">127</td>
    <td align="center">4</td>
    <td align="center">40</td>
    <td align="center">143</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{handbag}}$</td>
    <td align="center">0.89</td>
    <td align="center">0.63</td>
    <td align="center">0.92</td>
    <td align="center">0.53</td>
    <td align="center">0.89</td>
    <td align="center">0.91</td>
  </tr>
      <tr>
    <td>$\color{orange}{\textsf{nrDetects}}$</td>
    <td>$\color{orange}{\textsf{train}}$</td>
    <td align="center">4</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0.72</td>
    <td align="center">0</td>
  </tr>
    <tr>
    <td>$\color{orange}{\textsf{avgConf}}$</td>
    <td>$\color{orange}{\textsf{train}}$</td>
    <td align="center">0.86</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
    <td align="center">0.00</td>
  </tr>
        <tr>
    <td colspan="2" align="center" >$\color{ORANGE}{\textsf{Total detections}}$</td>
    <td align="center">35356</td>
    <td align="center">34622</td>
    <td align="center">34897</td>
    <td align="center">32363</td>
    <td align="center">32439</td>
    <td align="center">44549</td>  
    </tr>
      <tr>
    <td colspan="2" align="center" >$\color{ORANGE}{\textsf{Average FPS}}$</td>
    <td align="center">216</td>
    <td align="center">136</td>
    <td align="center">285</td>
    <td align="center">150</td>
    <td align="center">107</td>
    <td align="center">75</td>  
    </tr>
  <tr>
    <td colspan="2" align="center" >$\color{orange}{\textsf{GPU}}$</td>
    <td colspan="7" align="center" >$\color{green}{\textsf{NVIDIA GeForce RTX 4090, 24209MiB}}$</td>
  </tr>
  
</table>

</details>

<details>
  <summary> Inference on video using yolov5m engine and pytorch weights </summary>

  ```bash
#engine weights
./YoloModelsInference.sh yolov5m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType engine  --count "car,person,bicycle,bus,traffic light" 
 ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/45b842e3-758b-4afe-9ae3-36125846cb7b)


![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/54e9df06-f6c9-401b-9efe-6ce78c932e4f)

  ```bash
#pytorch weights
 ./YoloModelsInference.sh yolov5m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType pytorch  --count "car,person,bicycle,bus,traffic light" 
 ```

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/79ad0b6d-8484-401b-9185-5dd2554104a3)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/d862cf11-e130-4653-bd95-6d8b1bcb17af)

</details>


<details>
  <summary> Inference on video using yolov6s engine and pytorch weights </summary>

  ```bash
#engine weights
./YoloModelsInference.sh yolov6s --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType engine  --count "car,person,bicycle,bus,traffic light" 
 ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/45b842e3-758b-4afe-9ae3-36125846cb7b)


![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/344845ae-bd2b-42d3-a297-d34050492367)

  ```bash
#pytorch weights
 ./YoloModelsInference.sh yolov6m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType pytorch  --count "car,person,bicycle,bus,traffic light" 
 ```

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/79ad0b6d-8484-401b-9185-5dd2554104a3)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/82f32130-cbbd-438f-be8e-0f65145e5f95)

</details>


<details>
  <summary> Inference on video using yolov7 engine and pytorch weights </summary>

  ```bash
#engine weights
./YoloModelsInference.sh yolov7 --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType engine  --count "car,person,bicycle,bus,traffic light" 
 ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/7f851c87-c7f3-4583-9ffc-fb5eaa28b142)


![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/36951eb1-cb46-4308-99b8-f93c3a7e4fd2)

  ```bash
#pytorch weights
 ./YoloModelsInference.sh yolov7 --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType pytorch  --count "car,person,bicycle,bus,traffic light" 
 ```

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/f9fa971f-a28e-4c98-885b-19890cc471b0)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/a9ff4153-b846-4866-88b2-160b7cacd8bc)

</details>

<details>
  <summary> Inference on video using yolov8m engine and pytorch weights </summary>

  ```bash
#engine weights
./YoloModelsInference.sh yolov8m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType engine  --count "car,person,bicycle,bus,traffic light" 
 ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/8d37da0d-a60c-4f1c-ae91-7ef350c76151)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/067de1c9-2dc6-454e-8529-141e8c182323)

  ```bash
#pytorch weights
 ./YoloModelsInference.sh yolov8m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextColor "white" --labelTextSize 6 --weightsType pytorch  --count "car,person,bicycle,bus,traffic light" 
 ```

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/ee8e3011-c189-47d9-ae71-2181373ccc4b)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/191d3a7f-0a39-4983-adf6-22a8de5ed9b6)

</details>

<details>
  <summary> Inference on video using yolov9-m engine and pytorch weights </summary>

  ```bash
#engine weights
./YoloModelsInference.sh yolov9-m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType engine  --count "car,person,bicycle,bus,traffic light" 
 ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/90061c46-6542-4bec-bd44-3db13ad46838)


![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/df46363a-7699-4546-90a8-e8f06b8fe671)

  ```bash
#pytorch weights
 ./YoloModelsInference.sh yolov9-m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType pytorch  --count "car,person,bicycle,bus,traffic light" 
 ```

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/2cae4226-9725-49b6-9c92-1f616ee5f146)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/df916696-7233-4e46-97d0-50f13b0f6a1a)

</details>

<details>
  <summary> Inference on video using gelan-m engine and pytorch weights </summary>

  ```bash
#engine weights
./YoloModelsInference.sh gelan-m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType engine  --count "car,person,bicycle,bus,traffic light" 
 ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/85338f36-725e-4a94-bfc9-c00ee65ff2a5)


![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/97c1ceb7-5716-4469-ab5e-cdb4a16f5b49)

  ```bash
#pytorch weights
 ./YoloModelsInference.sh gelan-m --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType pytorch  --count "car,person,bicycle,bus,traffic light" 
 ```

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/a3a06584-9ab3-4aed-ae41-81ed4f2056be)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/247261c8-5002-4892-b705-66a5027665f4)

</details>


<details>
  <summary> Inference on video using yolov10b engine and pytorch weights </summary>

  ```bash
#engine weights
./YoloModelsInference.sh yolov10b --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType engine  --count "car,person,bicycle,bus,traffic light" 
 ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/b0ca25e4-dd37-44ef-8274-7366216f16e8)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/227eb041-ec3f-41fd-8a63-9108867ed41f)

  ```bash
#pytorch weights
 ./YoloModelsInference.sh yolov10b --video_index 1 --fontSize 1.8 --fontThickness 3 --ypos 50 --initialypos 20 --labelTextSize 6 --weightsType pytorch  --count "car,person,bicycle,bus,traffic light" 
 ```

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/20fa6841-c21c-4997-9877-d20a427bddc3)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/285a6aab-8eba-4cc2-b3ca-16f623262602)

</details>
<details>
  <summary> Inference on video using yolo11x engine and pytorch weights </summary>

  ```bash
#engine weights
./YoloModelsInference.sh yolo11x --video_index 2 --fontSize 1.2 --fontThickness 3 --ypos 36 --initialypos 20 --labelTextSize 4 --weightsType engine  --count "car,person,bicycle,bus,truck,train,traffic light"
 ```
![image](https://github.com/user-attachments/assets/f266201a-5be4-4529-a6b5-6319f3a74475)

![image](https://github.com/user-attachments/assets/6b963ceb-61bf-49f7-b850-9a6238cf919d)

  ```bash
#pytorch weights
./YoloModelsInference.sh yolo11x --video_index 2 --fontSize 1.2 --fontThickness 3 --ypos 36 --initialypos 20 --labelTextSize 4 --weightsType pytorch  --count "car,person,bicycle,bus,truck,train,traffic light"
 ```
![image](https://github.com/user-attachments/assets/436389d8-7666-486d-b68d-b212bf511821)

![image](https://github.com/user-attachments/assets/7d435681-6232-4427-86b1-60fd3a5449ca)

</details>
</details>

## Comparison Evaluation Metrics

<details>
  <summary> Total number of detections for each class and average score precision using engine weights  </summary>

![image](https://github.com/user-attachments/assets/8e13dadb-d0ac-489a-9323-62dc48e136e1)

![image](https://github.com/user-attachments/assets/dc53173d-e6ef-43d4-9a9a-3f9ee2341ad7)

</details>
<details>
  <summary> Total number of detections for each class and average score precision using pytorch weights  </summary>
  
![image](https://github.com/user-attachments/assets/356cd440-5ca3-4f06-a295-6cb357d6332d)

![image](https://github.com/user-attachments/assets/6eb62e7b-0fbf-4ee6-a632-618b2e04897a)

</details>


The results are also stored in [GoodleDrive](https://drive.google.com/drive/folders/1Owg6Gd3stiNBYRch9avVK_r4GuGfNJOk?usp=sharing).

