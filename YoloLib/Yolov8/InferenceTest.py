import os
import yaml
import cv2
import glob
import random
from ultralytics import YOLO
import cv2
import os
import time

# video_to_infer = os.listdir('VideoPredictNEW')
model_weights = os.listdir('runs/detect')

j = 10
k = 0
# for i in range(0, len(video_to_infer)):
# for j in range(0, len(model_weights)):
start_time = time.time()
# path1 = 'uns/detect/' + model_weights[j]
# path2 = os.listdir(path1)
# model_path = path1 + "/" + path2[k]

# video_path = '/content/drive/MyDrive/YoloV8_FireDetection_/Video_to_predict/PredictVideo/' + video_to_infer[i]

video = 'video4.mp4'
video_path = '/home/constantin/Doctorat/FireDataset/TestVideos/TestVideo6.mp4'

# save_pth ='/content/drive/MyDrive/YoloV8_FireDetection_/inference2/yolov8s' + model_weights[j] + '_' + 'fire1'

# print('************inference with model: {} on video: {} is started!*******************'. format(model_weights[j],video_path ))
model =YOLO('/home/constantin/Doctorat/YoloModels/YoloLib/Yolov8/runs/detect/final_DS_yolov8s4/weights/best_80epochs.pt')
start_time = time.time()
results = model(source ='/home/constantin/Doctorat/FireDataset/FireTestImages/', show = False, conf = 0.4, save =True, device = 0)
# save_pth = model_weights[j] + '_' + 'fire18'

seconds = time.time() - start_time
print("-----Inference time is: -------", seconds)
inference_time = "-----Inference time is: ------- {}".format(seconds)
# write_path = 'runs/detect/predict{}/{}.txt'.format(counter, save_pth)

# with open(write_path, 'w') as file:
#   file.write(inference_time)

  # counter+=1

# predict_pathh = os.listdir('runs/detect/')
# predict_path = 'runs/detect/'
# for p in predict_pathh:
#     if p == 'predict':
#         dstt = model_weights[j] + "-" + path2[k] + '-'+video
#         src = f"{predict_path}/{p}"  # foldername/filename, if .py file is outside folder
#         dst = f"{predict_path}/{dstt}"
#
#         # rename() function will
#         # rename all the files
#         os.rename(src, dst)
