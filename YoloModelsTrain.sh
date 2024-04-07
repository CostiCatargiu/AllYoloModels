#!/bin/bash

datasetPath="/home/constantin/Doctorat/FireDataset/RoboflowDS/yolov6/data.yaml"
epochs=2
batchSize=64

# Function to display usage information
usage() {
    echo "Usage: $0 <required param> [optional_param1] [optional_param2]"
    echo "Parameters:"
    echo "  required_param: YoloModel that want to train: egg. yolov5s, yolov5m, yolov6s, yolov7, yolov8s, yolov8m, yolov9, yolonas"
    echo "  optional_param1 (datasetPath): default: = $datasetPath"
    echo "  optional_param2 (epochs): default: = $epochs"
    echo "  optional_param3 (batchSize): default: = $batchSize"
}

# Check if the required parameter is provided
if [ "$#" -eq 0 ]; then
    usage
    exit 1
fi

# Assign required parameter to a variable
select_model="$1"
shift

# Parse optional parameters
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -p1|--datasetPath)
            datasetPath="$2"
            shift 2
            ;;
        -p2|--epochs)
            epochs="$2"
            shift 2
            ;;
       -p3|--batchSize)
            batchSize="$2"
            shift 2
            ;;
        *)  # Unknown option
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

current_location=$(pwd)
experimetsPath=$current_location/ExperimentalResults

if [[ "$select_model" == *"yolov5"* ]]; then
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV5/weights/$select_model.pt
    fi
    cd "$current_location/YoloModels/YoloV5/"
    python3 train.py \
        --epochs $epochs \
        --batch-size $batchSize\
        --data $datasetPath \
        --cfg models/$select_model.yaml \
        --weights $weights \
        --project $experimetsPath/YoloV5/train \
        --name exp

elif [[ "$select_model" == *"yolov6"* ]]; then
    cd "$current_location/YoloModels/YoloV6/"
    python3 train.py \
        --epochs $epochs \
        --batch-size $batchSize \
        --conf $current_location/YoloModels/YoloV6/configs/$select_model.py \
        --data $datasetPath \
        --device 0 \
        --eval-interval 10 \
        --output-dir $experimetsPath/YoloV6/train \
        --name exp

elif [[ "$select_model" == *"yolov7"* ]]; then
    cd "$experimetsPath/YoloV7/weights/"
    weights_url="https://github.com/WongKinYiu/yolov7/releases/download/v0.1/$select_model.pt"
    if [ -f "$select_model.pt" ]; then
        echo "Weights $select_model.pt exists..."
    else
        echo "Download weights $select_model.pt..."
        curl -L -o "$select_model.pt" "$weights_url"
    fi
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV7/weights/$select_model.pt
    fi
    cd "$current_location/YoloModels/YoloV7/"
    python3 train.py \
        --epochs $epochs \
        --batch-size $batchSize \
        --cfg cfg/training/$select_model.yaml \
        --data $datasetPath \
        --weights $weights \
        --project $experimetsPath/YoloV7/train \
        --name exp

elif [[ "$select_model" == *"yolov8"* ]]; then
     if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV8/weights/$select_model.pt
    fi
    yolo \
        task=detect \
        mode=train \
        model=$weights \
        data=$datasetPath \
        epochs=$epochs \
        batch=$batchSize\
        project=$experimetsPath/YoloV8/train \
        name=exp

elif [[ "$select_model" == *"yolov9"* && "$select_model" != *"converted"* ]]; then    # Source file path
    cd "$experimetsPath/YoloV9/weights/"
    weights_url="https://github.com/WongKinYiu/yolov9/releases/download/v0.1/$select_model.pt"
    if [ -f "$select_model.pt" ]; then
        echo "Weights $select_model.pt exists..."
    else
        echo "Download weights $select_model.pt..."
        curl -L -o "$select_model.pt" "$weights_url"
    fi
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV9/weights/$select_model.pt
    fi
    cd "$current_location/YoloModels/YoloV9/"
    python3 train_dual.py \
        --epochs $epochs \
        --batch-size $batchSize \
        --data $datasetPath \
        --cfg $current_location/YoloModels/YoloV9/models/detect/$select_model.yaml \
        --hyp hyp.scratch-high.yaml  \
        --weights $weights \
        --project $experimetsPath/YoloV9/train\
        --name exp

elif [[ "$select_model" == *"gelan"* || "$select_model" == *"converted"* ]]; then    # Source file path
    cd "$experimetsPath/YoloV9/weights/"
    weights_url="https://github.com/WongKinYiu/yolov9/releases/download/v0.1/$select_model.pt"
    if [ -f "$select_model.pt" ]; then
        echo "Weights $select_model.pt exists..."
    else
        echo "Download weights $select_model.pt..."
        curl -L -o "$select_model.pt" "$weights_url"
    fi
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV9/weights/$select_model.pt
    fi
    cd "$current_location/YoloModels/YoloV9/"
    python3 train.py \
        --epochs $epochs \
        --batch-size $batchSize \
        --data $datasetPath \
        --cfg $current_location/YoloModels/YoloV9/models/detect/$select_model.yaml \
        --hyp hyp.scratch-high.yaml  \
        --weights $weights \
        --project $experimetsPath/YoloV9/train\
        --name exp

else
    echo "Invalid model. Please provide either 'yolov5', 'yolov6', 'yolov7', 'yolov8', 'yolov9' or 'yolonas'."
fi
