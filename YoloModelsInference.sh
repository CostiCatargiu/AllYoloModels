#!/bin/bash

source UtilFunctions.sh
##Delete cache labels
#delete_cache

datasetPath=$(yq e '.datasetPath' parameters.yaml)
conf_thr=0.1
device=0
thr_metric=0.4
fontSize=1.0
fontThickness=4
ypos=40
labelColor="black"
labelSize=2
video_index=2

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
listvideos=$(list_videos)
source_video=$(get_video_path $video_index)

usage() {
    echo "Usage: $0 <required param> [optional_param1] [optional_param2] [optional_param3] [optional_param4] [optional_param5] [optional_param6]"
    echo "Parameters:"
    echo "  required_param: YoloModel that want to use for inference: [yolov5n, yolov5s, yolov5m, yolov5l, yolov5x], [yolov6n, yolov6s, yolov6m, yolov6l]"
    echo "  required_param: YoloModel that want to use for inference: [yolov7, yolov7-x, yolov7-w6, yolov7-d6, yolov7-e6e]"
    echo "  required_param: YoloModel that want to use for inference: [yolov8n, yolov8s, yolov8m, yolov8l, yolov8x], [yolov9-c, yolov9-e, gelan-c, gelan-e]"
    echo "  optional_param1 (-p1|| --weights): default: = /ExperimentalResults/YoloV.../weights/model.pt"
    echo "  optional_param2 (-p2|| --source_video): default: = $source_video or choose one video from the list by it index $listvideos"
    echo "  optional_param3 (-p3|| --conf_thr): default: = $conf_thr"
    echo "  optional_param4 (-p4|| --device): default: = $device"
    echo "  optional_param5 (-p5|| --count): default: = None"
    echo "  optional_param6 (-p6|| --filter): default: = None"
    echo "  optional_param7 (-p7|| --fontSize): default: = 1"
    echo "  optional_param8 (-p8|| --fontThickness): default: = 4"
    echo "  optional_param9 (-p9|| --ypos): default: = 40"
    echo "  optional_param10 (-p10|| --thr_metric): default: = 0.3"
    echo "  optional_param11 (-p11|| --labelColor): default: = 'black'"
    echo "  optional_param12 (-p12|| --labelSize): default: = 2"
    echo "  optional_param12 (-p13|| --video_index): default: = 2"
}

# Parse optional parameters
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -p2|--source_video)
            source_video="$2"
            shift 2
            ;;
        -p3|--conf_thr)
            conf_thr="$2"
            shift 2
            ;;
        -p1|--weights)
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
        -p7|--fontSize)
            fontSize=("$2")
            shift 2
            ;;
        -p8|--fontThickness)
            fontThickness="$2"
            shift 2
            ;;
        -p9|--ypos)
            ypos="$2"
            shift 2
            ;;
        -p10|--thr_metric)
            thr_metric="$2"
            shift 2
            ;;
        -p11|--labelColor)
            labelColor="$2"
            shift 2
            ;;
        -p12|--labelSize)
            labelSize="$2"
            shift 2
            ;;
        -p13|--video_index)
            video_index="$2"
            shift 2
            ;;
        *)  # Unknown option
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

source_video=$(get_video_path $video_index)


# Export the list as an environment variable if provided
if [ ${#count[@]} -gt 0 ]; then
    export COUNT_LIST="${count[@]}"
    export COUNT_FLAG=$'ok'
fi

if [ ${#filter[@]} -gt 0 ]; then
    export FILTER_LIST="${filter[@]}"
fi

current_location=$(pwd)
experimetsPath=$current_location/ExperimentalResults
inferenceScriptsPath=$current_location/InferenceScripts/
cpu_name=$(cat /proc/cpuinfo | grep "model name" | head -n1 | cut -d ":" -f2 | sed 's/^ *//')
gpu_name=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -n1)

export PARAMETER="$select_model"
export VIDEO_PATH="$source_video"
export CONF_THR="$conf_thr"
export METRIC_THR="$thr_metric"
export LABEL_SIZE="$labelSize"
export LABEL_COLOR="$labelColor"


export FONT_SCALE="$fontSize"
export FONT_THICKNESS="$fontThickness"
export POS_SCALE="$ypos"

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
    source_file="$inferenceScriptsPath/YoloV5/InferenceYoloV5.py"
    destination_directory="$current_location/YoloModels/YoloV5"
    source_file1="$inferenceScriptsPath/YoloV5/plots.py"
    destination_directory1="$current_location/YoloModels/YoloV5/utils"
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
    source_file="$inferenceScriptsPath/YoloV6/InferenceYoloV6.py"
    destination_directory="$current_location/YoloModels/YoloV6"
    source_file1="$inferenceScriptsPath/YoloV6/inferer.py"
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
    source_file="$inferenceScriptsPath/YoloV7/InferenceYoloV7.py"
    destination_directory="$current_location/YoloModels/YoloV7"
    source_file1="$inferenceScriptsPath/YoloV7/plots.py"
    destination_directory1="$current_location/YoloModels/YoloV7/utils"
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
        --conf-thres $conf_thr\
        --device $device


elif [[ "$select_model" == *"yolov8"* ]]; then
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV8/weights/$select_model.pt
    fi
    source_file1="$inferenceScriptsPath/YoloV6/InferenceYoloV8.py"
    source_file="$inferenceScriptsPath/YoloV6/predictor.py"
    source_file3="$inferenceScriptsPath/YoloV6/results.py"
    destination_directory="$current_location/YoloModels/YoloV8/ultralytics/engine/"
    destination_directory1="$current_location/YoloModels/YoloV8/"
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
    source_file="$inferenceScriptsPath/YoloV9/InferenceYoloV9dual.py"
    destination_directory="$current_location/YoloModels/YoloV9"
    source_file1="$inferenceScriptsPath/YoloV9/plots.py"
    destination_directory1="$current_location/YoloModels/YoloV9/utils"
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
    source_file="$inferenceScriptsPath/YoloV9/InferenceYoloV9gelan.py"
    destination_directory="$current_location/YoloModels/YoloV9"
    source_file1="$inferenceScriptsPath/YoloV9/plots.py"
    destination_directory1="$current_location/YoloModels/YoloV9/utils"
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
