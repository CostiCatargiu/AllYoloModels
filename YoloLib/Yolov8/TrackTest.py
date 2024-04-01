from ultralytics import YOLO
import os
# # Load an official or custom model
# model = YOLO('yolov8n.pt')  # Load an official Detect model
# model = YOLO('yolov8n-seg.pt')  # Load an official Segment model
# model = YOLO('yolov8n-pose.pt')  # Load an official Pose model

model_weights = os.listdir('BestWeights')

j = 8
k = 0

video_path = '/home/constantin/Doctorat/VideoFire/VideoNoFire/Video1.mp4'
path1 = 'BestWeights/' + model_weights[j]
path2 = os.listdir(path1)
model_path = 'runs/detect/new_yolov8m_train6/weights/best_80epochs.pt'

model = YOLO(model_path)  # Load a custom trained model


# Perform tracking with the model
results = model.track(source=video_path, show=False, save = True, name ='runs/detect')  # Tracking with default tracker
# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")  # Tracking with ByteTrack tracker