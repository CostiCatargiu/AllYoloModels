from ultralytics import YOLO

# Load a model
data = '/home/constantin/Doctorat/FireDataset/Rob`oflowDS/Yolov8_2/DSall/data.yaml',
model = YOLO('/home/constantin/Doctorat/YoloModels/YoloLib/Yolov8/runs/detect/final_DS_yolov8s6/weights/best_80epochs.pt')  # load a custom model

# Validate the model
metrics = model.val(conf = 0.75, split='test', half = False)  # no arguments needed, dataset and settings remembered
metrics.box.map    # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps   # a list contains map50-95 of each category

# import torch
# print(torch.cuda.is_available())

# python3 path/to/yolov8 detect --source path/to/test/images --weights path/to/trained/weights --save-json