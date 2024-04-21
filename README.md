# AllYoloModels
![output_filename](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/a8979dcb-2bb6-4f15-b4f9-10b3f99a7452)



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
After the model is cloned it will appear in $\color{magenta}{\textsf{YoloModels}}$ directory. If the model is already there and the script is executed a message will appear and ask if we want to reclone or no.

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/ac73a342-45ef-4668-a298-0d481387bc18)

</details>


## Evaluation task

 $\color{red}{\textsf{YoloModelsEval.sh}}$ file shall be used for this task. This file will trigger the evaluation script for the selected model.

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

  </tr>
  <tr>
    <td>$\color{orange}{\textsf{maP@0.50}}$</td>
    <td align="center">0.69</td>
    <td align="center">0.69</td>
    <td align="center">0.69</td>
    <td align="center">0.71</td>
    <td align="center">0.73</td>
    <td align="center">0.72</td>

  </tr>
    <tr>
    <td>$\color{orange}{\textsf{maP@0.50-95}}$</td>
    <td align="center">0.52</td>
    <td align="center">0.52</td>
    <td align="center">0.50</td>
    <td align="center">0.57</td>
    <td align="center">0.56</td>
    <td align="center">0.55</td>
    
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
    <td>$\color{orange}{\textsf{batchSize}}$</td>
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

  </tr>
  <tr>
    <td>$\color{orange}{\textsf{GPU}}$</td>
    <td colspan="7" align="center" >$\color{green}{\textsf{NVIDIA GeForce RTX 4090, 24209MiB}}$</td>
  </tr>
  
</table>

<details>
  <summary>Dowmload COCO dataset</summary>

To download COCO dataset you can use $\color{red}{\textsf{Utility/DatasetDownloadScripts/getcoco.sh}}$ .

The dataset will be downloaded in $\color{red}{\textsf{Utility/COCOdatasets}}$.

Please note that the labels for the testing set are not available, or at least I didn't find them. Another observation is that for YoloV6, we need to use bounding box format labels instead of polygon format labels for the evaluation task.

In the **get_coco.sh** script, we can select between downloading the train, test, valid, and segment data. By default, all datasets will be downloaded.

The YAML file for COCO dataset is located at path $\color{red}{\textsf{Utility/YAMLconfigs/coco.yaml}}$

Dataset size is around 27GB ( 5000 valid images, 40 670 test images and 118 287 train images)
</details>

<details>
  <summary>To see more detailed results obtained on evaluation task please see above.</summary>


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

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/069538f6-fa61-462f-bcb9-f95a871dca38)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/df790ffa-62d5-4ccf-a07d-6943d733b5f7)


</details>

<details>
  <summary>Evaluation on COCO dataset using yolov9-e </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/cb58d821-0462-4c93-93f6-e110cdf0582e)

</details>

<details>
  <summary>Evaluation on COCO dataset using yolov9_gelan-e </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/451f47b8-ca6a-40b8-ac9b-5e5ef451738f)

</details>

</details>

## Inference task

 $\color{red}{\textsf{YoloModelsInference.sh}}$ file shall be used for this task. This file will trigger the inference script for the selected model.

Syntax:

./YoloModelsInference.sh  <<select_model>> --[weights] val --[source_video] val --[conf_thr] val --[device] "val" --[count] "class1,class2..." -[filter] "class1,class2..."

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

#modify the labelTextColor, labelTextSize and video_index(choose another video for inference from the list)
./YoloModelsInference.sh gelan-c --conf_thr 0.2 --labelTextColor "blue" --labelTextSize 3 --video_index 4
or
./YoloModelsInference.sh gelan-c --conf_thr 0.2 -p11 "blue" -p12 3 -p13 4

```
Parameters: 
 << >> = required parameter; [ ]=optional parameter
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/d9df86a7-8ced-4f9c-acb5-3ca25d144793)

If you want to add more parameters to inference task please edit the $\color{red}{\textsf{YoloModelsInference.sh}}$ for the desired model.


<details>
  <summary>$\color{magenta}{\textsf{Short explanation of parameters usage}}$</summary>
  

The image above shows a variety of parameters available for selection, depending on what we aim to achieve in the inference task.
1. $\color{orange}{\textsf{model}}$: the only mandatory parameter required to initiate the inference process. It specifies the version of the YOLO model to be used for the inference task. The available options for this parameter are shown in the image above. All subsequent parameters are optional, and default values will be used if they are not provided.
   
2. $\color{orange}{\textsf{-p1 || --weights}}$: This parameter specifies the path to the weights that wiil be used for the inference. Default value for this:  $\color{blue}{\textsf{/ExperimentalResults/YoloV.../weights/<model>.pt}}$.

3. $\color{orange}{\textsf{p2 || --source video}}$: This parameter specifies the path to the video that will be used for inference. To simplify the selection of the desired video for inference, all files have been placed in a specific directory. From there, one can choose a video by indicating its index in the list (the image above displays all my test videos along with their respective indexes). The index of the video is specified using the next parameter.

4. $\color{orange}{\textsf{-p3 || --video index}}$: This parameter is used to indicate the list index of the video that will be used for inference.

5. $\color{orange}{\textsf{-p4 || --conf thr}}$: This parameter is used to set the cofindence threshold for the detection. Will be processed only the predictions with a precision greater than this threshold.

6. $\color{orange}{\textsf{-p5 || --device}}$: This parameter indicates the devide which will be used for the inference. We can choose 0 for GPU or "cpu".

7. $\color{orange}{\textsf{-p6 || --count}}$: This parameter is essentially a list where you can specify certain classes that the model was trained on. Using this parameter allows you to count and display the number of detections for the specified classes in each frame. By default this option is disabled.

8. $\color{orange}{\textsf{-p7 || --filter}}$: This parameter is essentially a list where you can specify certain classes that the model was trained on. Using this parameter allows you to exclude the specified classes from being displayed in the inference output. By default, this option is disabled.

9. $\color{orange}{\textsf{-p8 || --fontSize}}$: This parameter allows you to configure the text dimensions of the information displayed during video inference. This is useful because video resolutions can vary, and the text may be too small or too large depending on the resolution.

10. $\color{orange}{\textsf{-p9 || --fontThickness}}$: Similar to the previous parameter.

11.  $\color{orange}{\textsf{-p10 || --ypos}}$: This parameter is related to -p8 and -p9 and allows you to modify the distance between lines of displayed information to better fit within the image.

12. $\color{orange}{\textsf{-p11 || --thr metric}}$: This parameter sets a threshold for the metrics calculated after the inference process, based on the number of predictions per class and their confidence levels. Upon completion of the inference, a txt file with two tables will be generated: one displaying the number of predictions and their average precision for each class with a confidence greater than this threshold, and a second table with the same information for predictions with a confidence below this threshold.

13. $\color{orange}{\textsf{-p12 || --labelTextColor}}$: This parameter allows you to change the label text color, which can be useful when the text color is hard to distinguish from the background.

14. $\color{orange}{\textsf{-p13 || --labelTextSize}}$: This parameter allows you to adjust the label text size, which can be useful for different video resolutions where the text on certain labels may not be clearly visible.

</details>

$\color{darkorange}{\textsf{Advantages of this implementation:}}$

<details>
  <summary> -💻 During inference, details such as the device used, model, number of frames, FPS, and inference time are displayed on the output video. These details help monitor and assess the performance of the inference process. Additionally, there are customization options available to better fit the data on the video, such as adjusting the text size, thickness, and vertical positioning. </summary>

  ```bash
./YoloModelsInference.sh yolov8m --conf_thr 0.45 --count "car,person,bus,bicycle"  --labelTextColor "black" --fontSize 2 --fontThickness 2 --ypos 60 --video_index 15 --labelTextSize 2  --thr_metric 0.6
  ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/cb0cc011-6ceb-4e74-87ee-90d2098981f1)

  ```bash
./YoloModelsInference.sh yolov8m --conf_thr 0.45 --count "car,person,bus,bicycle"  --labelTextColor "white" --fontSize 1 --fontThickness 2 --ypos 40 --video_index 15 --labelTextSize 5  --thr_metric 0.6
  ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/24b5c096-174d-4c6a-ae24-a972a2ce1ba7)

</details>


<details>
  <summary> - 👁️‍🗨️ We can monitor the number of appearances of a certain object class across the frames. </summary>
  
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/794b4565-5737-4563-aa48-a4592150f248)

</details>

  <details>
  <summary> - 🚫 We can filter the detection of a certain class if it is not of interest to us. </summary>
    
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/22e8d381-8147-442e-a5b2-d47521270cc2)

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
  <summary> gelan-c.txt </summary>
    
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/b054d0c3-ef28-47d5-a58a-ac82757db83b)
  </details>
  
  <details>
  <summary> yolov9-c.txt </summary>
    
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/6e551a20-267b-41a2-9514-ffd48862ae26)
  </details>

  <details>
  <summary>yolov8l.txt </summary>
    
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/52ba1563-b2be-457e-b34b-81ebe03b9c05)
  </details>


Additionally, there's an option to create a separate TXT file that compares the results obtained from each model after inference.The key advantage of this new TXT file is that it structures the data into tables, enabling straightforward and efficient comparison of performance across different models. This tabular arrangement simplifies the analysis, allowing users to quickly assess and contrast the effectiveness of each model based on two metrics: average precision per class and total number of detection per class. This organized format is especially beneficial for identifying the most suitable model for specific tasks or environments.

To generate this new metric we need to follow 2 steps:
1. Put the .txt files that you want to compare at the following path: $\color{darkorange}{\textsf{ExperimentalResults/Metrics/}}$
2. Execute the .py script:  $\color{darkorange}{\textsf{Utils/Scripts/generatemetric.py}}$. The script will generate a $\color{darkorange}{\textsf{Utils/Scripts/metric.txt}}$ file that contains the compared data for the models selected. 

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/53e29bad-6973-4a1b-b2a8-42ce2cbcec6d)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/c2c9ef05-6995-4f2e-b367-81746292b071)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/e26c6719-186e-4c3f-9c54-0711828111f0)


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
  <summary> Inference on video using yolov5l </summary>

  ```bash
./YoloModelsInference.sh yolov5l --conf_thr 0.05 --count "car,person,bus,truck,traffic light"  --labelTextColor "black" --fontSize 2 --fontThickness 3 --ypos 60 --video_index 15 --labelTextSize 3 --thr_metric 0.5
 ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/8c4fd189-b7a0-46ad-8347-f3fc6290f143)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/7987c937-5777-46e4-922d-d1090858f72a)

</details>

<details>
  <summary> Inference on video using yolov6l </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/cfae5500-eb5e-4006-99cc-2d3187ad0b62)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/4d5b2a1e-23c7-4640-99f7-47ee4432ff03)

</details>


<details>
  <summary> Inference on video using yolov7 </summary>

  ```bash
./YoloModelsInference.sh yolov7 --conf_thr 0.05 --count "car,person,bus,truck,traffic light"  --labelTextColor "black" --fontSize 2 --fontThickness 3 --ypos 60 --video_index 15 --labelTextSize 3 --thr_metric 0.5
 ```
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/d2c5609b-e5ea-468b-b369-86ef17f6b40d)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/896a1e9f-de91-4e1d-941f-b9cc048a90f8)

</details>

<details>
  <summary> Inference on video using yolov8l </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/079c2685-8089-4ad4-8a1b-39047a52ac6c)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/cbe0c65a-0299-4eda-83f1-d10af1b5c34f)

</details>


<details>
  <summary> Inference on video using yolov9-c </summary>
  
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/d526fe75-dc57-4f45-af5e-05ac709c047a)
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/fa12797c-a2e5-4c24-b13c-2304479031c2)


</details>

<details>
  <summary> Inference on video using yolov9-gelan-c </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/26bcecde-4552-4622-978a-29d1bd587891)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/88f164f1-9f9d-48b5-8470-e7a419bd9134)

</details>
</details>
