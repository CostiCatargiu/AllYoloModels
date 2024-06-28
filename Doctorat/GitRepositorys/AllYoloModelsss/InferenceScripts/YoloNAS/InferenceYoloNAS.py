from super_gradients.training import models
import torch
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from UtilFunctions import CalcFPS, average_conf, avg_time, show_details


dataset_params = {
   'data_dir':'/home/constantin/Doctorat/FireDataset/RoboflowDS/YOLOV8/',
   'train_images_dir':'train/images',
   'train_labels_dir':'train/labels',
   'val_images_dir':'valid/images',
   'val_labels_dir':'valid/labels',
   'test_images_dir':'test/images',
   'test_labels_dir':'test/labels',
   'classes': ['fire', 'other', 'smoke']
}

parentpath= '//home/constantin/Doctorat/FireDataset/VideoTestFire/FireDay/'
input_video_path = parentpath+"VideoNightMixt.mp4"
output_video_path = parentpath+"VideoNightMixtNAS.mp4"

device = 0 if torch.cuda.is_available() else "cpu"
best_weights_path = "/home/constantin/Doctorat/YoloModels/YoloLib2/ExperimentalResults/YoloNAS/train/RUN_20240214_083607_689848/average_model.pth"
best_model = models.get('yolo_nas_s',
                        num_classes=len(dataset_params['classes']),
                        checkpoint_path=best_weights_path).to(device)

with open("/home/constantin/Doctorat/YoloModels/YoloLib2/ExperimentalResults/YoloNAS/infer/results.txt", 'w') as f:
    f.write("")

predictions = best_model.predict(input_video_path)
predictions.save(output_video_path)

with open("/home/constantin/Doctorat/YoloModels/YoloLib2/ExperimentalResults/YoloNAS/infer/results.txt", 'r') as f:
    data = f.read()

entries = data.split(',')

# Step 3: Process each entry to create the list of lists
list_of_lists = []
for entry in entries:
    if entry.strip():  # Check if the entry is not empty
        # Split the entry by spaces and group into sublists
        elements = entry.strip().split()
        sublist = []
        for i in range(0, len(elements), 2):
            sublist.append(f"{elements[i]} {elements[i + 1]}")
        list_of_lists.append(sublist)

coord_list = []
path = '/home/constantin/Doctorat/YoloModels/YoloLib2/ExperimentalResults/YoloNAS/infer/'
average_conf(list_of_lists, coord_list, path)