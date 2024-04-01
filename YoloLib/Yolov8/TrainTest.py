from ultralytics import YOLO

# Load the model.
model = YOLO('yolov8s.pt')

# Training.
results = model.train(
    data='/home/constantin/Doctorat/FireDataset/RoboflowDS/Yolov8_2/DSall/data.yaml',
    imgsz=640,
    epochs=50,
    batch=100,
    name='final_DS_yolov8s',
    dropout=0.0,

    patience =20,
    verbose = True
)

