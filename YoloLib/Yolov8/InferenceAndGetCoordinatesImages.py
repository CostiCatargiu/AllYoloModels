import os

from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated

model = YOLO('/home/constantin/Doctorat/YoloModels/YoloLib/Yolov8/runs/detect/new_yolov8m_train6/weights/best_80epochs.pt')

images_src_path = '/home/constantin/Doctorat/FireDatasetNewVideos/ImagesCopied/'
labels_save_path = '/home/constantin/Doctorat/FireDatasetNewVideos/LabelsAnnotated/'
images_save_path_annotated = '/home/constantin/Doctorat/FireDatasetNewVideos/ImagesAnnot/'
images_name = os.listdir(images_src_path)
counter = 0

for imgg in images_name:

    image = images_src_path + imgg
    image_info_annot = images_save_path_annotated + imgg
    img = cv2.imread(image)
    results = model.predict(img, conf = 0.2, iou = 0.3)
    label_name = imgg.split(".")[0] + '.txt'
    label_info = labels_save_path + label_name

    for r in results:
        annotator = Annotator(img)
        boxes = r.boxes
        with open(label_info, 'w') as file:
            file.write('')
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
            c = box.cls
            annotator.box_label(b, model.names[int(c)])
            clas = int(c[0].tolist())
            list_coords = box.xywhn[0].tolist()
            list_annot = []
            list_annot.append(clas)
            info = str(clas)
            for l in list_coords:
                list_annot.append(l)
                info = info + ' ' + str(l)

            with open(label_info, 'a') as file:
                file.write(info + '\n')
    counter +=1
    img = annotator.result()
    cv2.imwrite(image_info_annot, img)  # save frame as JPEG file

print(counter)