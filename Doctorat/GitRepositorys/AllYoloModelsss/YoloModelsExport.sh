#!/bin/bash

source UtilFunctions.sh
##Delete cache labels
#delete_cache

datasetPath=$(yq e '.datasetPath' parameters.yaml)
labelTextColor="white"
labelTextSize=2
exportType=engine

# Check if the required parameter is provided
if [ "$#" -eq 0 ]; then
    usage
    exit 1
fi

# Assign required parameter to a variable
select_model="$1"
shift


usage() {
    echo "Usage: $0 <required param> [optional_param1] ... [optional_param13]"
    echo "Parameters:"
    echo "  required_param: YoloModel that want to use for export: [yolov5n, yolov5s, yolov5m, yolov5l, yolov5x], [yolov6n, yolov6s, yolov6m, yolov6l]"
    echo "  required_param: YoloModel that want to use for inference: [yolov7, yolov7-x, yolov7-w6, yolov7-d6, yolov7-e6e]"
    echo "  required_param: YoloModel that want to use for inference: [yolov8n, yolov8s, yolov8m, yolov8l, yolov8x], [yolov9-c, yolov9-e, gelan-c, gelan-e]"
    echo "  optional_param1 (-p1 || --weights): default: = /ExperimentalResults/YoloV.../weights/model.pt"
    echo "  optional_param2 (-p2 || --exportType): default: = $exportType (choose between onnx and engine)"

}

# Parse optional parameters
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -p1|--weights)
            weights="$2"
            shift 2
            ;;
        -p2|--exportType)
            exportType="$2"
            shift 2
            ;;

        *)  # Unknown option
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done


export LABEL_SIZE="$labelTextSize"
export LABEL_COLOR="$labelTextColor"

current_location=$(pwd)
experimetsPath=$current_location/ExperimentalResults
inferenceScriptsPath=$current_location/InferenceScripts/

if [[ "$select_model" == *"yolov5"* ]]; then

    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV5/train/${weights}/weights/best.pt
    fi

    cd "$current_location/YoloModels/YoloV5/"
    if [[ "$exportType" == *"engine"* ]]; then
        python3 export.py \
          --weights $weight \
          --include $exportType \
          --device 0 \
          --half

    elif [[ "$exportType" == *"onnx"* ]]; then
        python3 export.py \
          --weights $weight \
          --include $exportType \
          --device 0
    fi

elif [[ "$select_model" == *"yolov8"* ]]; then

    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV8/train/${weights}/weights/best.pt
   elif [ -z "$weights" ]; then
      weight=$experimetsPath/YoloV8/weights/$select_model.pt
    fi

    cd "$current_location/YoloModels/YoloV5/"
    if [[ "$exportType" == *"engine"* ]]; then
      yolo export model=$weight \
            format=engine half=True \
            simplify opset=13 workspace=16

    elif [[ "$exportType" == *"onnx"* ]]; then
      yolo export model=$weight format=onnx simplify=False half=False
    fi

elif [[ "$select_model" == *"yolov9"* ]]; then

    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV9/train/${weights}/weights/best.pt
   elif [ -z "$weights" ]; then
      weight=$experimetsPath/YoloV9/weights/$select_model.pt
    fi

    cd "$current_location/YoloModels/YoloV9/"
    if [[ "$exportType" == *"engine"* ]]; then
        python3 export.py \
          --weights $weight \
          --data $datasetPath \
          --include $exportType \
          --device 0 \
          --half

    elif [[ "$exportType" == *"onnx"* ]]; then
        python3 export.py \
          --weights $weight \
          --data $datasetPath \
          --include $exportType \
          --device 0
    fi


elif [[ "$select_model" == *"gelan"* ]]; then

    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV9/trainGelan/${weights}/weights/best.pt
   elif [ -z "$weights" ]; then
      weight=$experimetsPath/YoloV9/weightsGelan/$select_model.pt
    fi

    cd "$current_location/YoloModels/YoloV9/"
    if [[ "$exportType" == *"engine"* ]]; then
        python3 export.py \
          --weights $weight \
          --data $datasetPath \
          --include $exportType \
          --device 0 \
          --imgsz 640 \
          --half

    elif [[ "$exportType" == *"onnx"* ]]; then
        python3 export.py \
          --weights $weight \
          --data $datasetPath \
          --include $exportType \
          --device 0
    fi

elif [[ "$select_model" == *"yolov10"* ]]; then

    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV10/train/${weights}/weights/best.pt
   elif [ -z "$weights" ]; then
      weight=$experimetsPath/YoloV10/weights/$select_model.pt
    fi

    cd "$current_location/YoloModels/YoloV5/"
    if [[ "$exportType" == *"engine"* ]]; then
      yolo export model=$weight \
            format=engine half=True \
            simplify opset=13 workspace=16

    elif [[ "$exportType" == *"onnx"* ]]; then
      yolo export model=$weight \
            format=onnx opset=13 simplify
    fi

else
    echo "Invalid model. Please provide either 'yolov5', 'yolov6', 'yolov7', 'yolov8', 'yolov9' or 'yolonas'."
fi

