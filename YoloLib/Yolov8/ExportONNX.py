from ultralytics import YOLO

# Load a model
model = YOLO('/home/constantin/Doctorat/YoloModels/Yolov8/runs/detect/new_yolov8m_train6/weights/best_80epochs.pt')  # load a custom trained model

# Export the model
model.export(format='onnx')