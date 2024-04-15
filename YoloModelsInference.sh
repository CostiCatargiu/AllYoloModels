#!/bin/bash

source UtilFunctions.sh

datasetPath=$(yq e '.datasetPath' parameters.yaml)
source_video="/home/constantin/Doctorat/FireDataset/VideoFire/VideoNoFire/testvideo4.mp4"

conf_thr=0.7
device=0

#Delete cache labels
delete_cache

# Function to display usage information
usage() {
    echo "Usage: $0 <required param> [optional_param1] [optional_param2] [optional_param3] [optional_param4] [optional_param5] [optional_param6]"
    echo "Parameters:"
    echo "  required_param: YoloModel that want to use for eval: egg. yolov5s, yolov5m, yolov6s, yolov7, yolov8s, yolov8m, yolov9-c, gelan-c, yolonas"
    echo "  optional_param1 (weights): default: = /ExperimentalResults/YoloV.../weights/model.pt"
    echo "  optional_param2 (source_video): default: = $source_video"
    echo "  optional_param3 (conf_thr): default: = $conf_thr"
    echo "  optional_param4 (device): default: = $device"
    echo "  optional_param5 (count): default: = None"
    echo "  optional_param6 (filter): default: = None"

}


# Check if the required parameter is provided
if [ "$#" -eq 0 ]; then
    usage
    exit 1
fi

# Assign required parameter to a variable
select_model="$1"
shift

count=()
filter=()

# Parse optional parameters
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -p1|--source_video)
            source_video="$2"
            shift 2
            ;;
        -p2|--conf_thr)
            conf_thr="$2"
            shift 2
            ;;
        -p3|--weights)
            weights="$2"
            shift 2
            ;;
        -p4|--device)
            device="$2"
            shift 2
            ;;
        -p5|--count)
            count+=("$2")  # Append each string to the list
            shift 2
            ;;
        -p6|--filter)
            filter+=("$2")  # Append each string to the list
            shift 2
            ;;
        *)  # Unknown option
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

# Export the list as an environment variable if provided
if [ ${#count[@]} -gt 0 ]; then
    export COUNT_LIST="${count[@]}"
    export COOUNT_FLAG=$'ok'
fi

if [ ${#filter[@]} -gt 0 ]; then
    export FILTER_LIST="${filter[@]}"
fi

num_frames=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 "$source_video")
current_location=$(pwd)
experimetsPath=$current_location/ExperimentalResults
inferenceScriptsPath=$current_location/InferenceScripts/
cpu_name=$(cat /proc/cpuinfo | grep "model name" | head -n1 | cut -d ":" -f2 | sed 's/^ *//')
gpu_name=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -n1)

export PARAMETER="$select_model"
export NR_FRAMES="$num_frames"

if [[ "$device" == *"cpu"* ]]; then
  device_name=$cpu_name
else
  device_name=$gpu_name
fi

export DEVICE_PARAMETER="$device_name"


if [[ "$select_model" == *"yolov5"* ]]; then
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV5/weights/$select_model.pt
    fi
    source_file="$inferenceScriptsPath/InferenceYoloV5.py"
    destination_directory="$current_location/YoloModels/YoloV5"
    cp "$source_file" "$destination_directory"
    cd "$current_location/YoloModels/YoloV5/"
    python3 InferenceYoloV5.py \
        --data $datasetPath \
        --weights $weights \
        --source $source_video \
        --conf-thres $conf_thr \
        --project $experimetsPath/YoloV5/infer \
        --name exp \
        --device $device \
        --view-img

elif [[ "$select_model" == *"yolov6"* ]]; then
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV6/weights/$select_model.pt
    fi
    source_file="$inferenceScriptsPath/InferenceYoloV6.py"
    destination_directory="$current_location/YoloModels/YoloV6"
    source_file1="$inferenceScriptsPath/inferer.py"
    destination_directory1="$current_location/YoloModels/YoloV6/yolov6/core/"
    cp "$source_file" "$destination_directory"
    cp "$source_file1" "$destination_directory1"
    cd "$current_location/YoloModels/YoloV6/"
    python3 InferenceYoloV6.py \
        --weights $weights \
        --source $source_video \
        --conf-thres $conf_thr \
        --project $experimetsPath/YoloV6/infer\
        --name exp \
        --view-img \
        --device $device

elif [[ "$select_model" == *"yolov7"* ]]; then
    source_file="$inferenceScriptsPath/InferenceYoloV7.py"
    destination_directory="$current_location/YoloModels/YoloV7"
    cp "$source_file" "$destination_directory"
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
    python3 InferenceYoloV7.py \
        --weights $weights \
        --source $source_video \
        --project $experimetsPath/YoloV7/infer \
        --name exp \
        --view-img \
        --conf-thres $conf_thr
        --device $device


elif [[ "$select_model" == *"yolov8"* ]]; then
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV8/weights/$select_model.pt
    fi
    source_file1="$inferenceScriptsPath/InferenceYoloV8.py"
    source_file="$inferenceScriptsPath/predictor.py"
    source_file2="$inferenceScriptsPath/plotting.py"
    source_file3="$inferenceScriptsPath/results.py"
    destination_directory="$current_location/YoloModels/YoloV8/ultralytics/engine/"
    destination_directory1="$current_location/YoloModels/YoloV8/"
    destination_directory2="$current_location/YoloModels/YoloV8/ultralytics/utils/"
    cp "$source_file" "$destination_directory"
    cp "$source_file1" "$destination_directory1"
    cp "$source_file2" "$destination_directory2"
    cp "$source_file3" "$destination_directory"
    cd "$current_location/YoloModels/YoloV8/"
    python3 InferenceYoloV8.py \
        --weights $weights\
        --source $source_video \
        --conf-thres $conf_thr \
        --project $experimetsPath/YoloV8/infer \
        --name exp \
        --device $device

elif [[ "$select_model" == *"yolov9"* && "$select_model" != *"converted"* ]]; then    # Source file path
    source_file="$inferenceScriptsPath/InferenceYoloV9dual.py"
    destination_directory="$current_location/YoloModels/YoloV9"
    cp "$source_file" "$destination_directory"
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
    python3 InferenceYoloV9dual.py \
        --data /home/constantin/Doctorat/FireDataset/RoboflowDS/Yolov5/DSall/data.yaml \
        --weights $weights \
        --source $source_video \
        --conf-thres $conf_thr \
        --project $experimetsPath/YoloV9/infer \
        --name exp \
        --view-img \
        --device $device

elif [[ "$select_model" == *"gelan"* || "$select_model" == *"converted"* ]]; then    # Source file path
    source_file="$inferenceScriptsPath/InferenceYoloV9gelan.py"
    destination_directory="$current_location/YoloModels/YoloV9"
    cp "$source_file" "$destination_directory"
    cd "$experimetsPath/YoloV9/weightsGelan/"
    weights_url="https://github.com/WongKinYiu/yolov9/releases/download/v0.1/$select_model.pt"
    if [ -f "$select_model.pt" ]; then
        echo "Weights $select_model.pt exists..."
    else
        echo "Download weights $select_model.pt..."
        curl -L -o "$select_model.pt" "$weights_url"
    fi
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV9/weightsGelan/$select_model.pt
    fi
    cd "$current_location/YoloModels/YoloV9/"
    python3 InferenceYoloV9gelan.py \
        --data /home/constantin/Doctorat/FireDataset/RoboflowDS/Yolov5/DSall/data.yaml \
        --weights $weights \
        --source $source_video \
        --conf-thres $conf_thr \
        --project $experimetsPath/YoloV9/inferGelan \
        --name exp \
        --view-img \
        --device $device


else
    echo "Invalid model. Please provide either 'yolov5', 'yolov6', 'yolov7', 'yolov8', 'yolov9' or 'yolonas'."
fi
