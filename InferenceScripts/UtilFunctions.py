import supervision as sv
from supervision.geometry.core import Point
from supervision.draw.utils import draw_text
import os, cv2
from collections import deque
import numpy as np
from collections import defaultdict

frames = 0
def set_parameters():
    yolo_model = os.environ.get('PARAMETER')
    device_name = os.environ.get('DEVICE_PARAMETER')
    nrFrames = os.environ.get('NR_FRAMES')
    classesCount = os.environ.get('COUNT_LIST', '').split(',')
    if 'NVIDIA' in device_name:
        text_anchor5 = Point(x=90, y=20)
    else:
        text_anchor5 = Point(x=135, y=20)
    text_anchor4 = Point(x=65, y=50)
    text_anchor = Point(x=40, y=80)
    text_anchor1 = Point(x=115, y=80)
    text_anchor2 = Point(x=30, y=110)
    text_anchor3 = Point(x=80, y=110)

    text_overlay = f'InfTime:'
    text_overlay2 = f'FPS:'
    text_overlay4 = f'Model: {yolo_model}'
    text_overlay5 = f'{device_name}'
    text_overlay6 = f'{device_name}'

    text_anchor8 = Point(x=40, y=140)
    text_anchor9 = Point(x=95, y=140)
    text_overlay8 = f'frames:'
    text_anchor10 = Point(x=150, y=140)
    text_overlay10 = f':{nrFrames}'

    text_scale = 0.6
    text_thickness = 2
    text_color = sv.Color.ROBOFLOW
    background_color = sv.Color.WHITE

    anchor_list =[]
    anchor_list1 =[]
    for i in range(0, len(classesCount)):
        if len(classesCount[i]) > 4:
            anchor_list.append(Point(x=40+len(classesCount[i])*2, y=(175+(i*37))))
            anchor_list1.append(Point(x=90+len(classesCount[i])*4, y=(175 + (i * 37))))
            yPos=175 + (i * 37)
        else:
            anchor_list.append(Point(x=40 + len(classesCount[i]), y=(175 + (i * 37))))
            anchor_list1.append(Point(x=85 + len(classesCount[i]), y=(175 + (i * 37))))
            yPos=175 + (i * 37)

    text_anchor6 = Point(x=50, y=yPos+38)
    text_anchor7 = Point(x=95, y=yPos+38)
    text_overlay7 = f'total:'



    return text_anchor8, text_anchor9, text_anchor10, text_overlay8,text_overlay10, text_anchor6, text_anchor7, text_overlay7, anchor_list1, anchor_list, classesCount, text_anchor, text_anchor1, text_anchor2, text_anchor3,text_anchor5, text_anchor4, text_overlay5, text_overlay6, text_overlay, text_overlay2,text_overlay4,text_color,text_scale,text_thickness,background_color


def show_inference(text_anchor8, text_anchor9, text_anchor10, text_overlay8,text_overlay10, text_anchor6, text_anchor7,text_overlay7, anchor_list1, anchor_list, classesCount, inference_time, avg_fps, im0, p, text_anchor, text_anchor1, text_anchor2, text_anchor3,text_anchor5, text_anchor4, text_overlay5,text_overlay6, text_overlay, text_overlay2,text_overlay4,text_color,text_scale,text_thickness,background_color, dets):
    global frames
    frames +=1
    avg_fps = int(round(avg_fps))
    inference_time_ms = inference_time * 1000
    text_overlay3 = f'{avg_fps}'
    text_overlay1 = f'{inference_time_ms:.2f}'
    annotated_frame = draw_text(scene=im0, text=text_overlay, text_anchor=text_anchor,
                                text_color=text_color, background_color=background_color,
                                text_thickness=text_thickness, text_scale=text_scale)
    annotated_frame = draw_text(scene=annotated_frame, text=text_overlay1, text_anchor=text_anchor1,
                                text_color=text_color, background_color=background_color,
                                text_thickness=text_thickness, text_scale=text_scale)
    annotated_frame = draw_text(scene=annotated_frame, text=text_overlay2, text_anchor=text_anchor2,
                                text_color=text_color, background_color=background_color,
                                text_thickness=text_thickness, text_scale=text_scale)
    annotated_frame = draw_text(scene=annotated_frame, text=text_overlay3, text_anchor=text_anchor3,
                                text_color=text_color, background_color=background_color,
                                text_thickness=text_thickness, text_scale=text_scale)
    annotated_frame = draw_text(scene=annotated_frame, text=text_overlay4, text_anchor=text_anchor4,
                                text_color=sv.Color.RED, background_color=background_color,
                                text_thickness=1, text_scale=0.5)
    annotated_frame = draw_text(scene=annotated_frame, text=text_overlay5, text_anchor=text_anchor5,
                                text_color=sv.Color.RED, background_color=background_color,
                                text_thickness=1, text_scale=0.4)

    annotated_frame = draw_text(scene=annotated_frame, text=text_overlay8, text_anchor=text_anchor8,
                                text_color=sv.Color.BLACK, background_color=background_color,
                                text_thickness=1, text_scale=0.5)
    annotated_frame = draw_text(scene=annotated_frame, text=f"{frames}", text_anchor=text_anchor9,
                                text_color=sv.Color.BLACK, background_color=background_color,
                                text_thickness=1, text_scale=0.5)
    annotated_frame = draw_text(scene=annotated_frame, text=text_overlay10, text_anchor=text_anchor10,
                                text_color=sv.Color.BLACK, background_color=background_color,
                                text_thickness=1, text_scale=0.5)

    countFlag = os.environ.get('COOUNT_FLAG')
    if countFlag =='ok':
        nr_dets = []
        for i in range(0, len(classesCount)):
            ok = 0
            for j in range(0, (len(dets))):
                if dets[j] == classesCount[i] or str(dets[j])[:-1] == classesCount[i]:
                    nr_dets.append(str(dets[j-1]))
                    ok = 1
            if ok == 0:
                nr_dets.append('0')

        # print(nr_dets)
        # res = [eval(i) for i in nr_dets]

        # total_det=sum(nr_dets)
        total_det = sum([int(i) for i in nr_dets if type(i)== int or i.isdigit()])
        total_det = str(total_det)
        for i in range(0, len(classesCount)):
            annotated_frame = draw_text(scene=annotated_frame, text=classesCount[i]+':', text_anchor=anchor_list[i],
                                    text_color=sv.Color.RED, background_color=background_color,
                                    text_thickness=2, text_scale=0.6)

        for i in range(0, len(classesCount)):
            annotated_frame = draw_text(scene=annotated_frame, text=nr_dets[i], text_anchor=anchor_list1[i],
                                    text_color=sv.Color.RED, background_color=background_color,
                                    text_thickness=2, text_scale=0.6)

        annotated_frame = draw_text(scene=annotated_frame, text=text_overlay7, text_anchor=text_anchor6,
                                text_color=sv.Color.RED, background_color=background_color,
                                text_thickness=2, text_scale=0.6)

        annotated_frame = draw_text(scene=annotated_frame, text=total_det, text_anchor=text_anchor7,
                                text_color=sv.Color.RED, background_color=background_color,
                                text_thickness=2, text_scale=0.6)

    # cv2.imshow("Image", annotated_frame)
    cv2.imshow(str(p), annotated_frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        exit(1)

    return annotated_frame


def average_conf(dets_list, conf_list):
    class_precisions = {}
    for dets_l, conf_l in zip(dets_list, conf_list):
        i = 0
        while i < len(dets_l):
            class_name = dets_l[i + 1]
            num_objects = int(dets_l[i])
            precision_sum = 0

            # Iterate through precision values for this class
            for j in range(num_objects):
                precision_sum += float(conf_l.pop(0))  # Pop and sum precision values

            # Calculate average precision for this class
            average_precision = precision_sum / num_objects

            # Assign average precision to the class
            if class_name in class_precisions:
                class_precisions[class_name].append(round(average_precision, 2))
            else:
                class_precisions[class_name] = [round(average_precision, 2)]

            i += 2  # Move to the next class in the list

    overall_averages = {}

    for class_name, precisions in class_precisions.items():
        overall_average = sum(precisions) / len(precisions)
        overall_averages[class_name] = round(overall_average, 2)

    print("The average precision per classes is:")
    print(overall_averages)


def class_counts(dets_list):
    class_counts = defaultdict(int)
    for item in dets_list:
        # Iterate over each pair of count and label
        for i in range(0, len(item), 2):
            count = int(item[i])
            label = item[i + 1]
            # Check if the label is in plural form
            if label.endswith('s') and label[:-1] in class_counts:
                # Unify the label by removing the 's'
                unified_label = label[:-1]
            else:
                unified_label = label
            class_counts[unified_label] += count

    class_counts_dict = dict(class_counts)
    print("Number of detections per class:")
    print(class_counts_dict)
    total_sum = sum(class_counts_dict.values())
    print("Total number of detections: ", total_sum)

def yolov8_statisctics(data_list):
    l1_list = []  # List of lists for classes and their counts
    l2_list = []  # List of lists for average precision scores

    for data in data_list:
        label_count = {}  # Dictionary to count occurrences of each label
        label_sum = {}  # Dictionary to store sum of confidence scores for each label
        l1 = []  # List for classes and their counts
        l2 = []  # List for average precision scores

        # Iterate over the current list
        for item in data:
            # Split each element into class and confidence score
            split_item = item.rsplit(' ', 1)
            class_name = split_item[0]
            confidence = float(split_item[1])

            # Update label count
            label_count[class_name] = label_count.get(class_name, 0) + 1

            # Update sum of confidence scores
            label_sum[class_name] = label_sum.get(class_name, 0) + confidence

        # Iterate over the label count dictionary to populate l1 and compute averages for l2
        for class_name, count in label_count.items():
            # Append count and class to l1
            l1.append(count)
            l1.append(class_name)

            # Compute average confidence score for the current class
            avg_confidence = round(label_sum[class_name] / count, 2)

            # Append average confidence score to l2
            l2.append(avg_confidence)
            l2.append(class_name)

        l1_list.append(l1)
        l2_list.append(l2)
    return l1_list, l2_list


def average_precision_classes_yolov8(list):
    # Dictionary to store cumulative confidence scores and counts for each class
    class_scores = {}

    # Iterate through each sublist in the data
    for sublist in list:
        # Iterate through each pair of confidence score and class
        for i in range(0, len(sublist), 2):
            confidence = sublist[i]
            class_name = sublist[i + 1]
            if class_name not in class_scores:
                class_scores[class_name] = [confidence, 1]  # Initialize with confidence score and count 1
            else:
                class_scores[class_name][0] += confidence  # Add confidence score
                class_scores[class_name][1] += 1  # Increment count

    # Calculate average confidence for each class and round to two decimal places
    class_averages = {class_name: round(score[0] / score[1], 2) for class_name, score in class_scores.items()}

    # Convert to list of tuples for sorting
    result_list = [(class_name, average) for class_name, average in class_averages.items()]

    # Sort the list by class name
    result_list.sort(key=lambda x: x[0])
    print("The average precision per classes is:")
    print(result_list)


class CalcFPS:
    def __init__(self, nsamples: int = 100):
        self.framerate = deque(maxlen=nsamples)

    def update(self, duration: float):
        self.framerate.append(duration)

    def accumulate(self):
        if len(self.framerate) > 1:
            return np.average(self.framerate)
        else:
            return 0.0