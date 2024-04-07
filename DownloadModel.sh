#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: $0 <required param> [optional_param1] [optional_param2]"
    echo "Parameters:"
    echo "  required_param: YoloModel that want to clone: egg. yolov5, yolov6, yolov7, yolov8, yolov9, yolonas"
}

# Check if the required parameter is provided
if [ "$#" -eq 0 ]; then
    usage
    exit 1
fi

# Assign required parameter to a variable
select_model="$1"
shift

current_location=$(pwd)
cd "$current_location/YoloModels/"

if [[ "$select_model" == *"yolov5"* ]]; then
    folder_path="$current_location/YoloModels/YoloV5"
    if [ -d "$folder_path" ]; then
        read -p "Folder already exists. Do you want to delete it and clone again? (y/n): " answer
        if [ "$answer" = "y" ]; then
            echo "Deleting existing folder..."
            rm -rf "$folder_path"
            git clone https://github.com/ultralytics/yolov5.git
            name="$current_location/YoloModels/yolov5"
            rename="$current_location/YoloModels/YoloV5"
            mv "$name" "$rename"
            cd "$current_location/YoloModels/YoloV5"
            pip install -r requirements.txt
        else
            echo "Exiting without cloning."
        fi
    else
      git clone https://github.com/ultralytics/yolov5.git
      name="$current_location/YoloModels/yolov5"
      rename="$current_location/YoloModels/YoloV5"
      mv "$name" "$rename"
      cd "$current_location/YoloModels/YoloV5"
      pip install -r requirements.txt
    fi

elif [[ "$select_model" == *"yolov6"* ]]; then
    folder_path="$current_location/YoloModels/YoloV6/"
    if [ -d "$folder_path" ]; then
        read -p "Folder already exists. Do you want to delete it and clone again? (y/n): " answer
        if [ "$answer" = "y" ]; then
            echo "Deleting existing folder..."
            rm -rf "$folder_path"
            git clone https://github.com/meituan/YOLOv6.git
            name="$current_location/YoloModels/YOLOv6"
            rename="$current_location/YoloModels/YoloV6"
            mv "$name" "$rename"
            cd "$current_location/YoloModels/YoloV6"
            pip install -r requirements.txt
        else
            echo "Exiting without cloning."
        fi
    else
      git clone https://github.com/meituan/YOLOv6.git
      name="$current_location/YoloModels/YOLOv6"
      rename="$current_location/YoloModels/YoloV6"
      mv "$name" "$rename"
      cd "$current_location/YoloModels/YoloV6"
      pip install -r requirements.txt
    fi
    inferFile="$current_location/YoloModels/YoloV6/tools/infer.py"
    evalFile="$current_location/YoloModels/YoloV6/tools/eval.py"
    trainFile="$current_location/YoloModels/YoloV6/tools/train.py"
    dstPath="."
    cp "$inferFile" "$dstPath"
    cp "$evalFile" "$dstPath"
    cp "$trainFile" "$dstPath"


elif [[ "$select_model" == *"yolov7"* ]]; then
    folder_path="$current_location/YoloModels/YoloV7"
    if [ -d "$folder_path" ]; then
        read -p "Folder already exists. Do you want to delete it and clone again? (y/n): " answer
        if [ "$answer" = "y" ]; then
            echo "Deleting existing folder..."
            rm -rf "$folder_path"
            git clone https://github.com/WongKinYiu/yolov7.git
            name="$current_location/YoloModels/yolov7"
            rename="$current_location/YoloModels/YoloV7"
            mv "$name" "$rename"
            cd "$current_location/YoloModels/YoloV7"
            pip install -r requirements.txt
        else
            echo "Exiting without cloning."
        fi
    else
      git clone https://github.com/WongKinYiu/yolov7.git
      name="$current_location/YoloModels/yolov7"
      rename="$current_location/YoloModels/YoloV7"
      mv "$name" "$rename"
      cd "$current_location/YoloModels/YoloV7"
      pip install -r requirements.txt
    fi

elif [[ "$select_model" == *"yolov8"* ]]; then
    folder_path="$current_location/YoloModels/YoloV8"
    if [ -d "$folder_path" ]; then
        read -p "Folder already exists. Do you want to delete it and clone again? (y/n): " answer
        if [ "$answer" = "y" ]; then
            echo "Deleting existing folder..."
            rm -rf "$folder_path"
            git clone https://github.com/ultralytics/ultralytics.git
            name="$current_location/YoloModels/ultralytics"
            rename="$current_location/YoloModels/YoloV8"
            mv "$name" "$rename"
            cd "$current_location/YoloModels/YoloV8"
#            pip install ultralytics
        else
            echo "Exiting without cloning."
        fi
    else
      git clone https://github.com/ultralytics/ultralytics.git
      name="$current_location/YoloModels/ultralytics"
      rename="$current_location/YoloModels/YoloV8"
      mv "$name" "$rename"
      cd "$current_location/YoloModels/YoloV8"
#      pip install ultralytics        else
    fi

elif [[ "$select_model" == *"yolov9"* ]]; then
    folder_path="$current_location/YoloModels/YoloV9"
    if [ -d "$folder_path" ]; then
        read -p "Folder already exists. Do you want to delete it and clone again? (y/n): " answer
        if [ "$answer" = "y" ]; then
            echo "Deleting existing folder..."
            rm -rf "$folder_path"
            git clone https://github.com/WongKinYiu/yolov9.git
            name="$current_location/YoloModels/yolov9"
            rename="$current_location/YoloModels/YoloV9"
            mv "$name" "$rename"
            cd "$current_location/YoloModels/YoloV9"
            pip install -r requirements.txt
        else
            echo "Exiting without cloning."
        fi
    else
      git clone https://github.com/WongKinYiu/yolov9.git
      name="$current_location/YoloModels/yolov9"
      rename="$current_location/YoloModels/YoloV9"
      mv "$name" "$rename"
      cd "$current_location/YoloModels/YoloV9"
      pip install -r requirements.txt
    fi

elif [[ "$select_model" == *"yolovnas"* ]]; then
    git clone https://github.com/Deci-AI/super-gradients.git
    name="$current_location/YoloModels/yolov5"
    rename="$current_location/YoloModels/YoloV5"
    mv "$name" "$rename"
    cd "YoloV5"
    pip install -r requirements.txt

else
    echo "Invalid model. Please provide either 'yolov5', 'yolov6', 'yolov7', 'yolov8', 'yolov9' or 'yolonas'."
fi


