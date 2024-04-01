import os
from moviepy.editor import VideoFileClip
from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated

model = YOLO('/home/constantin/Doctorat/YoloModels/YoloLib/Yolov8/runs/detect/new_yolov8m_train6/weights/best_80epochs.pt')
video_path = '/home/constantin/Doctorat/FireDatasetNEWVideos2/Videos2/'
videos = os.listdir(video_path)

frame_time = 0
for v in range(0, len(videos)):
    video_parse = video_path + videos[v]
    xname = videos[v].split(".")[0]
    print("Parse video :", video_parse )
    cap = cv2.VideoCapture(video_parse)
    cap.set(3, 640)
    cap.set(4, 640)
    count = 0
    nr = 0
    labels_save_path = '/home/constantin/Doctorat/FireDatasetNEWVideos2/Labels2/'
    images_save_path = '/home/constantin/Doctorat/FireDatasetNEWVideos2/Images2/'
    images_save_path_annotated = '/home/constantin/Doctorat/FireDatasetNEWVideos2/ImagesAnnot2/'

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps

    # clip = VideoFileClip(video_parse)
    # duration = clip.duration
    # clip.close()

    if duration < 120:
        frame_time = 15
    if duration >= 120 and duration < 300:
        frame_time = 25
    if duration >= 300 and duration < 480:
        frame_time = 45
    if duration >= 480 and duration < 720:
        frame_time = 60
    if duration >= 720 and duration < 900:
        frame_time = 75
    if duration >= 900 and duration < 1140:
        frame_time = 90
    if duration >= 1140 and duration < 1500:
        frame_time = 120
    if duration >= 1500:
        frame_time = 150

    while True:
        _, img = cap.read()
        if img is None:
            break
        if count % frame_time == 0:
            ok=0
            results = model.predict(img, conf = 0.2, iou=0.4)
            for r in results:
                if r.boxes:
                    ok = 1
                    break
            if ok:
                image_name = '{}_f{}.jpg'.format(xname, nr)
                image_info = images_save_path + image_name
                image_info_annot = images_save_path_annotated + '/' + image_name
                cv2.imwrite(image_info, img)  # save frame as JPEG file
                # BGR to RGB conversion is performed under the hood
                # see: https://github.com/ultralytics/ultralytics/issues/2575
                label_name = '{}_f{}.txt'.format(xname, nr)
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
                nr += 1

                img = annotator.result()
                cv2.imwrite(image_info_annot, img)  # save frame as JPEG file

        count +=1
    print(count)
    cap.release()
    # cv2.destroyAllWindows()