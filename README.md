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
 #count the number of detection for classes in " "
 ./YoloModelsInference.sh yolov5l --count "car,person,bicycle,truck"  --conf_thr 0.5

#filter car class from predicitions
 ./YoloModelsInference.sh yolov9-c --count "person,bicycle,truck" --filter "car"  --conf_thr 0.5 
```
Parameters: 
 << >> = required parameter; [ ]=optional parameter
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/ae41d194-6172-4cbe-ba14-d486dc399fd3)

If you want to add more parameters to inference task please edit the .sh for the desired model.

Advantages of this implementation:

<details>
  <summary> - 👁️‍🗨️ We can monitor the number of appearances of a certain object class across the frames. </summary>
  
  ![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/c8a32c40-6681-49d3-9d1b-bec396050ada)

</details>

  <details>
  <summary> - 🚫 We can filter the detection of a certain class if it is not of interest to us. </summary>
    
![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/56587703-b4a9-40b7-b0b3-7372348f9acc)

</details>

  <details>
  <summary>  - 📈 After the inference ends, some useful metrics will be outputted indicating the performance of the model. These metrics include: </summary>
    a. The total number of detections for each class over the frames.
    
    b. The average precision for each class over the frames.
    
    c. The average Frames Per Second (FPS).
    
    d. The total number of objects detected in the video.

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/b795eaf5-42e8-4905-8c2a-734ff1ac6f44)

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

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/f54e0662-2e1b-4dfa-b0af-e1857c752838)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/6c292903-44f4-4c30-8c39-084614a4f84d)

</details>

<details>
  <summary> Inference on video using yolov6l </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/cfae5500-eb5e-4006-99cc-2d3187ad0b62)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/4d5b2a1e-23c7-4640-99f7-47ee4432ff03)

</details>


<details>
  <summary> Inference on video using yolov7 </summary>

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/3cb56454-d93a-4188-926a-b50be3919708)

![image](https://github.com/CostiCatargiu/AllYoloModels/assets/70476115/468e023b-34d0-4544-ac47-9703f3111fb6)

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
