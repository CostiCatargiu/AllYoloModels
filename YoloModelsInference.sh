#!/bin/bash

source UtilFunctions.sh
##Delete cache labels
#delete_cache

datasetPath=$(yq e '.datasetPath' parameters.yaml)
conf_thr=0.4
device=0
thr_metric=0.6
fontSize=1.0
fontThickness=4
ypos=40
labelTextColor="white"
labelTextSize=2
video_index=2
initialypos=20
nrCompareFrames=4
boxSimilarity=5
saveConfusedPred=true

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
    echo "Usage: $0 <required param> [optional_param1] ... [optional_param13]"
    echo "Parameters:"
    echo "  required_param: YoloModel that want to use for inference: [yolov5n, yolov5s, yolov5m, yolov5l, yolov5x], [yolov6n, yolov6s, yolov6m, yolov6l]"
    echo "  required_param: YoloModel that want to use for inference: [yolov7, yolov7-x, yolov7-w6, yolov7-d6, yolov7-e6e]"
    echo "  required_param: YoloModel that want to use for inference: [yolov8n, yolov8s, yolov8m, yolov8l, yolov8x], [yolov9-c, yolov9-e, gelan-c, gelan-e]"
    echo "  optional_param1 (-p1 || --weights): default: = /ExperimentalResults/YoloV.../weights/model.pt"
    echo "  optional_param2 (-p2 || --source_video): default: = $source_video or choose one video from the list by it index $listvideos"
    echo "  optional_param3 (-p3 || --video_index): default: = $video_index"
    echo "  optional_param4 (-p4 || --conf_thr): default: = $conf_thr"
    echo "  optional_param5 (-p5 || --device): default: = $device"
    echo "  optional_param6 (-p6 || --count): default: = None"
    echo "  optional_param7 (-p7 || --filter): default: = None"
    echo "  optional_param8 (-p8 || --fontSize): default: = $fontSize"
    echo "  optional_param9 (-p9 || --fontThickness): default: = $fontThickness"
    echo "  optional_param10 (-p10 || --ypos): default: = $ypos"
    echo "  optional_param11 (-p11 || --initialypos): default: = $initialypos"
    echo "  optional_param12 (-p12 || --labelTextColor): default: = $labelTextColor. Options: "blue","green", "white", "black", "cyan", "magenta","gray", "roboflow""
    echo "  optional_param13 (-p13 || --labelTextSize): default: = $labelTextSize"
    echo "  optional_param14 (-p14 || --nrCompareFrames): default: = $nrCompareFrames"
    echo "  optional_param15 (-p15 || --saveConfusedPred): default: = $saveConfusedPred"

}

# Parse optional parameters
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -p1|--weights)
            weights="$2"
            shift 2
            ;;
        -p2|--source_video)
            source_video="$2"
            shift 2
            ;;
        -p3|--video_index)
            video_index="$2"
            shift 2
            ;;
        -p4|--conf_thr)
            conf_thr="$2"
            shift 2
            ;;

        -p5|--device)
            device="$2"
            shift 2
            ;;
        -p6|--count)
            count+=("$2")  # Append each string to the list
            shift 2
            ;;
        -p7|--filter)
            filter+=("$2")  # Append each string to the list
            shift 2
            ;;
        -p8|--fontSize)
            fontSize=("$2")
            shift 2
            ;;
        -p9|--fontThickness)
            fontThickness="$2"
            shift 2
            ;;
        -p10|--ypos)
            ypos="$2"
            shift 2
            ;;
        -p11|--initialypos)
            initialypos="$2"
            shift 2
            ;;
        -p12|--labelTextColor)
            labelTextColor="$2"
            shift 2
            ;;
        -p13|--labelTextSize)
            labelTextSize="$2"
            shift 2
            ;;
        -p14|--nrCompareFrames)
            nrCompareFrames="$2"
            shift 2
            ;;
        -p15|--saveConfusedPred)
            saveConfusedPred="$2"
            shift 2
            ;;
        -p16|--boxSimilarity)
            boxSimilarity="$2"
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
export LABEL_SIZE="$labelTextSize"
export LABEL_COLOR="$labelTextColor"
export INITIALYPOS="$initialypos"
export NR_COMPARE_FRAMES="$nrCompareFrames"
export BOX_SIMILARITY="$boxSimilarity"


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
    base_path = "ExperimentalResults/YoloVS/train/"
    if [ -z "$weights" ]; then
        weight=$experimetsPath/YoloV5/weights/$select_model.pt
    fi

    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV5/train/${weights}/weights/best.pt
    fi
    export WEIGHTS_USED="$weight"

    source_file="$inferenceScriptsPath/YoloV5/InferenceYoloV5.py"
    destination_directory="$current_location/YoloModels/YoloV5"
    source_file1="$inferenceScriptsPath/YoloV5/plots.py"
    destination_directory1="$current_location/YoloModels/YoloV5/utils"
    cp "$source_file" "$destination_directory"
    cp "$source_file1" "$destination_directory1"

    cd "$current_location/YoloModels/YoloV5/"
    python3 InferenceYoloV5.py \
        --data $datasetPath \
        --weights $weight \
        --source $source_video \
        --conf-thres $conf_thr \
        --project $experimetsPath/YoloV5/infer \
        --name exp \
        --device $device \
        --view-img
    cd "$inferenceScriptsPath"
      python3 ExtractFramesDuplicate.py $experimetsPath/YoloV5/infer

elif [[ "$select_model" == *"yolov6"* ]]; then
    if [ -z "$weights" ]; then
        weight=$experimetsPath/YoloV6/weights/$select_model.pt
    fi

    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV6/train/${weights}/weights/best_ckpt.pt
    fi
    export WEIGHTS_USED="$weight"

    source_file="$inferenceScriptsPath/YoloV6/InferenceYoloV6.py"
    destination_directory="$current_location/YoloModels/YoloV6"
    source_file1="$inferenceScriptsPath/YoloV6/inferer.py"
    destination_directory1="$current_location/YoloModels/YoloV6/yolov6/core/"
    cp "$source_file" "$destination_directory"
    cp "$source_file1" "$destination_directory1"
    cd "$current_location/YoloModels/YoloV6/"
    python3 InferenceYoloV6.py \
        --weights $weight \
        --source $source_video \
        --conf-thres $conf_thr \
        --project $experimetsPath/YoloV6/infer\
        --name exp \
        --view-img \
        --device $device \
        --yaml $datasetPath

        if [ "$saveConfusedPred" = "true" ]; then
          cd "$inferenceScriptsPath"
             python3 ExtractFramesDuplicate.py $experimetsPath/YoloV6/infer
        fi

elif [[ "$select_model" == *"yolov7"* ]]; then
    source_file="$inferenceScriptsPath/YoloV7/InferenceYoloV7.py"
    destination_directory="$current_location/YoloModels/YoloV7"
    source_file1="$inferenceScriptsPath/YoloV7/plots.py"
    destination_directory1="$current_location/YoloModels/YoloV7/utils"
    cp "$source_file" "$destination_directory"
    cp "$source_file1" "$destination_directory1"
    cd "$experimetsPath/YoloV7/weights/"
    weights_url="https://github.com/WongKinYiu/yolov7/releases/download/v0.1/$select_model.pt"
    if [ -f "$select_model.pt" ]; then
        echo "Weights $select_model.pt exists..."
    else
        echo "Download weights $select_model.pt..."
        curl -L -o "$select_model.pt" "$weights_url"
    fi
    if [ -z "$weights" ]; then
        weight=$experimetsPath/YoloV7/weights/$select_model.pt
    fi

    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV7/train/${weights}/weights/best.pt
    fi
    export WEIGHTS_USED="$weight"

    cd "$current_location/YoloModels/YoloV7/"
    python3 InferenceYoloV7.py \
        --weights $weight \
        --source $source_video \
        --project $experimetsPath/YoloV7/infer \
        --name exp \
        --view-img \
        --conf-thres $conf_thr\
        --device $device

        if [ "$saveConfusedPred" = "true" ]; then
        cd "$inferenceScriptsPath"
           python3 ExtractFramesDuplicate.py $experimetsPath/YoloV7/infer
        fi

elif [[ "$select_model" == *"yolov8"* ]]; then
    if [ -z "$weights" ]; then
        weight=$experimetsPath/YoloV8/weights/$select_model.pt
    fi

    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV8/train/${weights}/weights/best.pt
    fi
    export WEIGHTS_USED="$weight"

    source_file1="$inferenceScriptsPath/YoloV8/InferenceYoloV8.py"
    source_file="$inferenceScriptsPath/YoloV8/predictor.py"
    source_file3="$inferenceScriptsPath/YoloV8/results.py"
    destination_directory="$current_location/YoloModels/YoloV8/ultralytics/engine/"
    destination_directory1="$current_location/YoloModels/YoloV8/"
    cp "$source_file" "$destination_directory"
    cp "$source_file1" "$destination_directory1"
    cp "$source_file2" "$destination_directory2"
    cp "$source_file3" "$destination_directory"
    cd "$current_location/YoloModels/YoloV8/"
    python3 InferenceYoloV8.py \
        --weights $weight\
        --source $source_video \
        --conf-thres $conf_thr \
        --project $experimetsPath/YoloV8/infer \
        --name exp \
        --device $device

    if [ "$saveConfusedPred" = "true" ]; then
        cd "$inferenceScriptsPath"
           python3 ExtractFramesDuplicate.py $experimetsPath/YoloV8/infer
    fi


elif [[ "$select_model" == *"yolov9"* && "$select_model" != *"converted"* ]]; then    # Source file path
    source_file="$inferenceScriptsPath/YoloV9/InferenceYoloV9dual.py"
    destination_directory="$current_location/YoloModels/YoloV9"
    source_file1="$inferenceScriptsPath/YoloV9/plots.py"
    destination_directory1="$current_location/YoloModels/YoloV9/utils"
    cp "$source_file" "$destination_directory"
    cp "$source_file1" "$destination_directory1"
    cd "$experimetsPath/YoloV9/weights/"
    weights_url="https://github.com/WongKinYiu/yolov9/releases/download/v0.1/$select_model.pt"
    if [ -f "$select_model.pt" ]; then
        echo "Weights $select_model.pt exists..."
    else
        echo "Download weights $select_model.pt..."
        curl -L -o "$select_model.pt" "$weights_url"
    fi
    if [ -z "$weights" ]; then
        weight=$experimetsPath/YoloV9/weights/$select_model.pt
    fi

    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV9/train/${weights}/weights/best.pt
    fi
    export WEIGHTS_USED="$weight"

    cd "$current_location/YoloModels/YoloV9/"
    python3 InferenceYoloV9dual.py \
        --data /home/constantin/Doctorat/FireDataset/RoboflowDS/Yolov5/DSall/data.yaml \
        --weights $weight \
        --source $source_video \
        --conf-thres $conf_thr \
        --project $experimetsPath/YoloV9/infer \
        --name exp \
        --view-img \
        --device $device

    if [ "$saveConfusedPred" = "true" ]; then
      cd "$inferenceScriptsPath"
         python3 ExtractFramesDuplicate.py $experimetsPath/YoloV9/infer
    fi

elif [[ "$select_model" == *"gelan"* || "$select_model" == *"converted"* ]]; then    # Source file path
    source_file="$inferenceScriptsPath/YoloV9/InferenceYoloV9gelan.py"
    destination_directory="$current_location/YoloModels/YoloV9"
    source_file1="$inferenceScriptsPath/YoloV9/plots.py"
    destination_directory1="$current_location/YoloModels/YoloV9/utils"
    cp "$source_file" "$destination_directory"
    cp "$source_file1" "$destination_directory1"
    cd "$experimetsPath/YoloV9/weightsGelan/"
    weights_url="https://github.com/WongKinYiu/yolov9/releases/download/v0.1/$select_model.pt"
    if [ -f "$select_model.pt" ]; then
        echo "Weights $select_model.pt exists..."
    else
        echo "Download weights $select_model.pt..."
        curl -L -o "$select_model.pt" "$weights_url"
    fi
    if [ -z "$weights" ]; then
        weight=$experimetsPath/YoloV9/weightsGelan/$select_model.pt
    fi
    if [[ "$weights" == *"exp"* ]]; then
        weight=${current_location}/ExperimentalResults/YoloV9/trainGelan/${weights}/weights/best.pt
    fi
    export WEIGHTS_USED="$weight"

    cd "$current_location/YoloModels/YoloV9/"
    python3 InferenceYoloV9gelan.py \
        --data /home/constantin/Doctorat/FireDataset/RoboflowDS/Yolov5/DSall/data.yaml \
        --weights $weight \
        --source $source_video \
        --conf-thres $conf_thr \
        --project $experimetsPath/YoloV9/inferGelan \
        --name exp \
        --view-img \
        --device $device

    if [ "$saveConfusedPred" = "true" ]; then
        cd "$inferenceScriptsPath"
           python3 ExtractFramesDuplicate.py $experimetsPath/YoloV9/inferGelan
    fi

else
    echo "Invalid model. Please provide either 'yolov5', 'yolov6', 'yolov7', 'yolov8', 'yolov9' or 'yolonas'."
fi
