from supervision.draw.utils import draw_text
import os, cv2
from collections import deque
import numpy as np
from collections import defaultdict
import json
from ultralytics.utils.plotting import colors

fps_list=[]
inf_list = []
frames = 0
yolo_model = os.environ.get('PARAMETER')
conf_thr = os.environ.get('CONF_THR')
metric_thr = float(os.environ.get('METRIC_THR'))
device_name = os.environ.get('DEVICE_PARAMETER')
classesCount = os.environ.get('COUNT_LIST', '').split(',')
countFlag = os.environ.get('COUNT_FLAG')
fontScale = float(os.environ.get('FONT_SCALE'))
font_thickness = int(os.environ.get('FONT_THICKNESS'))
posScale = int(os.environ.get('POS_SCALE'))
video_path = ""
initialypos = int(os.environ.get('INITIALYPOS'))

def get_nr_frames():
    global video_path
    video_path = os.environ.get('VIDEO_PATH')
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open the video file.")
        exit()
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return total_frames

def draw_text(
        img,
        text,
        font=cv2.FONT_HERSHEY_SIMPLEX,
        pos=(0, 0),
        font_scale=2,
        font_thickness=2,
        text_color=(0, 255, 0),
        text_color_bg=(0, 0, 0)
):
    offset = (5, 5)
    x, y = pos
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    rec_start = tuple(x - y for x, y in zip(pos, offset))
    rec_end = tuple(x + y for x, y in zip((x + text_w, y + text_h), offset))
    cv2.rectangle(img, rec_start, rec_end, text_color_bg, -1)
    cv2.putText(
        img,
        text,
        (x, int(y + text_h + font_scale - 1)),
        font,
        font_scale,
        text_color,
        font_thickness,
        cv2.LINE_AA,
    )
    return text_size

def show_details(p, im0, dets, inference_time, avg_fps):
    global nrFrames, frames, yolo_model, conf_thr, metric_thr, device_name, classesCount, countFlag, font_thickness, fontScale, posScale, fps_list, inf_list, initialypos
    nrFrames = get_nr_frames()
    frames +=1
    avg_fps = int(round(avg_fps))
    fps_list.append(avg_fps)
    inference_time_ms = inference_time *1000
    inf_list.append(inference_time_ms)

    draw_text(im0, f"{device_name} | Model: {yolo_model}", pos=(20, initialypos), font_scale=fontScale,
              text_color=colors(15,True), text_color_bg=(255, 255, 255), font_thickness=font_thickness,)

    draw_text(im0, f"Frames: {frames}/{nrFrames} | FPS: {avg_fps:0.1f}  | Time: {inference_time_ms:0.1f}ms/frame", pos=(20, initialypos+posScale), font_scale=fontScale,
              text_color=(204, 85, 17), text_color_bg=(255, 255, 255), font_thickness=font_thickness,)

    if countFlag =='ok':
        nr_dets = []
        for i in range(0, len(classesCount)):
            ok = 0
            for j in range(0, (len(dets))):
                if dets[j] == classesCount[
                    i] or str(dets[j])[:-1] == classesCount[i]:
                    nr_dets.append(str(dets[j-1]))
                    ok = 1
            if ok == 0:
                nr_dets.append('0')

        # total_det=sum(nr_dets)
        total_det = sum([int(i) for i in nr_dets if type(i)== int or i.isdigit()])
        for i in range(0, len(classesCount)):
            draw_text(im0, f"{classesCount[i]}:{nr_dets[i]}",
                      pos=(20, initialypos+posScale*(i+2)), font_scale=fontScale,
                      text_color=colors(i,True), text_color_bg=(255, 255, 255), font_thickness=font_thickness, )

        draw_text(im0, f"total: {total_det}",
                  pos=(20, initialypos+posScale*(len(classesCount)+2)), font_scale=fontScale,
                  text_color=colors(i,True), text_color_bg=(255, 255, 255), font_thickness=font_thickness, )

    cv2.imshow(str(p), im0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit(1)
    return im0

def avg_time(path):
    inf_time_list = []
    avg_fps_list = []
    for i in range(10, len(inf_list)):
        rounded_inf = "{:.2f}".format(inf_list[i])
        inf_time_list.append(float(rounded_inf))

    for i in range(10, len(fps_list)):
        avg_fps_list.append(fps_list[i])

    total_sum = sum(avg_fps_list)
    average = total_sum / len(avg_fps_list)
    print("Average FPS: {}.".format(int(round(average))))
    inf_sum = sum(inf_time_list)
    average_inf = inf_sum / len(inf_time_list)
    average_inf = "{:.2f}".format(average_inf)
    print(f"Average InfTime: {average_inf}ms per frame.")
    total_inf_time = (float(average_inf) * int(nrFrames)) / 100
    total_inf_time = "{:.2f}".format(total_inf_time)
    print(f"Total Inference time:{total_inf_time}s")
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = os.path.join("/",path, f"{yolo_model}.txt")
    with open(file_path, "a") as f:
        f.write("\nAverage FPS: ")
        f.write(str(round(average)))
        f.write("\nAverage InfTime: ")
        f.write(str(average_inf))
        f.write("ms per frame.\n")
        f.write(f"Total inference time: {str(total_inf_time)}s for {str(nrFrames)} frames.")
        f.write(f"\nVideo used for inference: {video_path}")

def average_conf(dets_list, conf_list, path):
    # Initialize an empty dictionary to collect confidences for each class
    result_dict = {}

    thr_metric = metric_thr
    # Process each detection and confidence list
    for dets, confs in zip(dets_list, conf_list):
        index = 0  # This will track the current index in the confidence list
        for i in range(1, len(dets), 2):
            count = dets[i - 1]  # Number of confidences to take
            class_name = dets[i]  # Class name

            # Extract the confidences for this class
            conf_for_class = confs[index:index + int(count)]
            index += int(count)  # Move the index forward

            # Append these confidences to the corresponding class in the dictionary
            if class_name in result_dict:
                result_dict[class_name].extend(conf_for_class)
            else:
                result_dict[class_name] = conf_for_class

    # Calculate the average and count the total number of elements for each key
    average_dict1 = {key: (sum(map(float, values)) / len(values), len(values)) for key, values in result_dict.items()}

    # Calculate the average for each key for values greater than 0.6 and count these values
    average_dict2 = {}
    average_dict3 = {}
    average_dict4 = {}
    average_dict5 = {}
    average_dict6 = {}
    average_dict7 = {}
    average_dict8 = {}

    for key, values in result_dict.items():
        # Convert and filter values greater than 0.6
        filtered_values = list(filter(lambda x: x >= 0.9, map(float, values)))

        # Calculate average if there are any values greater than 0.6, otherwise set to None
        if filtered_values:
            average = round(sum(filtered_values) / len(filtered_values), 2)
        else:
            average = None  # Or set to 0 or any indicator that no values are above the threshold

        # Store the average and the count of values greater than 0.6
        average_dict2[key] = (average, len(filtered_values))


    for key, values in result_dict.items():
        # Convert and filter values greater than 0.6
        filtered_values = list(filter(lambda x: 0.8 <= x < 0.9, map(float, values)))

        # Calculate average if there are any values greater than 0.6, otherwise set to None
        if filtered_values:
            average = round(sum(filtered_values) / len(filtered_values), 2)
        else:
            average = None  # Or set to 0 or any indicator that no values are above the threshold

        # Store the average and the count of values lower than 0.6
        average_dict3[key] = (average, len(filtered_values))

    for key, values in result_dict.items():
        # Convert and filter values greater than 0.6
        filtered_values = list(filter(lambda x: 0.7 <= x < 0.8, map(float, values)))

        # Calculate average if there are any values greater than 0.6, otherwise set to None
        if filtered_values:
            average = round(sum(filtered_values) / len(filtered_values), 2)
        else:
            average = None  # Or set to 0 or any indicator that no values are above the threshold

        # Store the average and the count of values lower than 0.6
        average_dict4[key] = (average, len(filtered_values))

    for key, values in result_dict.items():
        # Convert and filter values greater than 0.6
        filtered_values = list(filter(lambda x: 0.6 <= x < 0.7, map(float, values)))

        # Calculate average if there are any values greater than 0.6, otherwise set to None
        if filtered_values:
            average = round(sum(filtered_values) / len(filtered_values), 2)
        else:
            average = None  # Or set to 0 or any indicator that no values are above the threshold

        # Store the average and the count of values lower than 0.6
        average_dict5[key] = (average, len(filtered_values))

    for key, values in result_dict.items():
        # Convert and filter values greater than 0.6
        filtered_values = list(filter(lambda x: 0.5 <= x < 0.6, map(float, values)))

        # Calculate average if there are any values greater than 0.6, otherwise set to None
        if filtered_values:
            average = round(sum(filtered_values) / len(filtered_values), 2)
        else:
            average = None  # Or set to 0 or any indicator that no values are above the threshold

        # Store the average and the count of values lower than 0.6
        average_dict6[key] = (average, len(filtered_values))

    for key, values in result_dict.items():
        # Convert and filter values greater than 0.6
        filtered_values = list(filter(lambda x: 0.4 <= x < 0.5, map(float, values)))

        # Calculate average if there are any values greater than 0.6, otherwise set to None
        if filtered_values:
            average = round(sum(filtered_values) / len(filtered_values), 2)
        else:
            average = None  # Or set to 0 or any indicator that no values are above the threshold

        # Store the average and the count of values lower than 0.6
        average_dict7[key] = (average, len(filtered_values))


    if not os.path.exists(path):
        os.makedirs(path)
    file_path = os.path.join("/", path, f"{yolo_model}.txt")

    total_values = sum(len(sublist) for sublist in conf_list)

    columns = ['Class', 'AvgP', 'NrDet']
    widths = [17, 14, 9]
    header = ' '.join(name.ljust(width) for name, width in zip(columns, widths))

    with open(file_path, "w") as f:
        print()
        output_string = f"Total number of detections:{int(total_values)} with a confidence threshold: {conf_thr}."
        print(output_string)
        f.write(output_string+'\n')
        print()

        output_string = f"Total number of detections for each class and average precision per class using a conf_thr={conf_thr}"
        print(output_string)
        f.write(output_string + '\n')
        print(header)
        f.write(header + '\n')

        # Print the average values and the total number of elements
        for key, (average, count) in average_dict1.items():
            row = f"{key.capitalize():<17} {average:<14.3f} {count:<9}"
            print(row)
            f.write(row + '\n')
        print()
        f.write("\n")

        output_string = f"Total number of detections and average of confidence score greater than 0.9 for each class."
        print(output_string)
        f.write(output_string + '\n')
        print(header)
        f.write(header + '\n')

        # Print the results with each label, its average, and count of values greater than 0.6
        for key, (average, count) in average_dict2.items():
            if average is None:
                average_display = "0"  #  text for None
            else:
                average_display = f"{average:.3f}"
            row = f"{key.capitalize():<17} {average_display:<14} {count:<9}"
            print(row)
            f.write(row + '\n')
        print()
        f.write("\n")

        output_string = f"Total number of detections and average of confidence score between 0.8 and 0.9 for each class."
        print(output_string)
        f.write(output_string)
        print(header)
        f.write('\n' + header + '\n')

        # Print the results with each label, its average, and count of values greater than 0.6
        for key, (average, count) in average_dict3.items():
            if average is None:
                average_display = "0"  # text for None
            else:
                average_display = f"{average:.3f}"
            row = f"{key.capitalize():<17} {average_display:<14} {count:<9} "
            print(row)
            f.write(row + '\n')
        print()

        output_string = f"\nTotal number of detections and average of confidence score between 0.7 and 0.8 for each class."
        print(output_string)
        f.write(output_string)
        print(header)
        f.write('\n' + header + '\n')

        # Print the results with each label, its average, and count of values greater than 0.6
        for key, (average, count) in average_dict4.items():
            if average is None:
                average_display = "0"  # text for None
            else:
                average_display = f"{average:.3f}"
            row = f"{key.capitalize():<17} {average_display:<14} {count:<9} "
            print(row)
            f.write(row + '\n')
        print()
        output_string = f"\nTotal number of detections and average of confidence score between 0.6 and 0.7 for each class."
        print(output_string)
        f.write(output_string)
        print(header)
        f.write('\n' + header + '\n')

        # Print the results with each label, its average, and count of values greater than 0.6
        for key, (average, count) in average_dict5.items():
            if average is None:
                average_display = "0"  # text for None
            else:
                average_display = f"{average:.3f}"
            row = f"{key.capitalize():<17} {average_display:<14} {count:<9} "
            print(row)
            f.write(row + '\n')
        print()

        output_string = f"\nTotal number of detections and average of confidence score between 0.5 and 0.6 for each class."
        print(output_string)
        f.write(output_string)
        print(header)
        f.write('\n' + header + '\n')

        # Print the results with each label, its average, and count of values greater than 0.6
        for key, (average, count) in average_dict6.items():
            if average is None:
                average_display = "0"  # text for None
            else:
                average_display = f"{average:.3f}"
            row = f"{key.capitalize():<17} {average_display:<14} {count:<9} "
            print(row)
            f.write(row + '\n')
        print()

        output_string = f"\nTotal number of detections and average of confidence score between 0.4 and 0.5 for each class."
        print(output_string)
        f.write(output_string)
        print(header)
        f.write('\n' + header + '\n')

        # Print the results with each label, its average, and count of values greater than 0.6
        for key, (average, count) in average_dict6.items():
            if average is None:
                average_display = "0"  # text for None
            else:
                average_display = f"{average:.3f}"
            row = f"{key.capitalize():<17} {average_display:<14} {count:<9} "
            print(row)
            f.write(row + '\n')
        print()


def class_counts(dets_list, path):
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
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = os.path.join("/",path, f"{yolo_model}.txt")
    with open(file_path, "w") as f:
        f.write("Number of detections per class: \n")
        json.dump(class_counts_dict, f)
        f.write("\nTotal number of detections: ")
        f.write(str(total_sum) + "\n")

def yolov8_statisctics(data_list):
    # Initialize lists to store the final results
    l1_final = []
    l2_final = []

    # Process each sublist independently
    for sublist in data_list:
        class_counts = {}
        precision_lists = {}

        # Process each item in the current sublist
        for item in sublist:
            # Split item at the last occurrence of a space to separate class label from precision
            last_space_index = item.rfind(' ')
            class_label = item[:last_space_index]
            precision = float(item[last_space_index + 1:])

            # Increment the count for each class
            if class_label in class_counts:
                class_counts[class_label] += 1
            else:
                class_counts[class_label] = 1

            # Append the precision to the list corresponding to the class
            if class_label in precision_lists:
                precision_lists[class_label].append(precision)
            else:
                precision_lists[class_label] = [precision]

        # Creating l1 for the current sublist
        l1 = []
        for class_label, count in sorted(class_counts.items()):
            l1.extend([count, class_label])
        l1_final.append(l1)

        # Creating l2 for the current sublist: a single list containing all precision values for this sublist
        l2 = []
        for class_label in sorted(precision_lists):
            l2.extend(precision_lists[class_label])
        l2_final.append(l2)

    # Output the lists
    # print("l1:", l1_final)
    # print("l2:", l2_final)
    return l1_final, l2_final

def average_precision_classes_yolov8(list, path):
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

    if not os.path.exists(path):
        os.makedirs(path)
    file_path = os.path.join("/",path, f"{yolo_model}.txt")
    with open(file_path, "a") as f:
        f.write("The average precision per classes is: \n")
        json.dump(result_list, f)


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