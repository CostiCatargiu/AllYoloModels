#!/bin/bash

source UtilFunctions.sh

datasetPath=$(yq e '.datasetPath' parameters.yaml)
confThr=0.001
iouThr=0.6
batchSize=32
imgSize=640
testSplit="valid"

#Delete cache labels
delete_cache

# Function to display usage information
usage() {
    echo "Usage: $0 <required param> [optional_param1] [optional_param2]"
    echo "Parameters:"
    echo "  required_param: (select_model)-YoloModel that want to use for eval: egg. yolov5s, yolov5m, yolov6s, yolov7, yolov8s, yolov8m, yolov9-c, gelan-c"
    echo "  optional_param1 (datasetPath): default: = $datasetPath"
    echo "  optional_param2 (weights): default: = /ExperimentalResults/YoloV.../weights/model.pt"
    echo "  optional_param3 (batchSize): default: = $batchSize"
    echo "  optional_param4 (confThr): default: = $confThr"
    echo "  optional_param4 (iouThr): default: = $iouThr"
    echo "  optional_param5 (img_size): default: = $imgSize"
    echo "  optional_param5 (testSplit): default: = $testSplit"
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
       -p2|--batchSize)
            batchSize="$2"
            shift 2
            ;;
       -p3|--confThr)
            confThr="$2"
            shift 2
            ;;
       -p4|--imgSize)
            imgSize="$2"
            shift 2
            ;;
       -p5|--weights)
            weights="$2"
            shift 2
            ;;
      -p6|--testSplit)
            testSplit="$2"
            shift 2
            ;;
      -p6|--iouThr)
            iouThr="$2"
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
inferenceScriptsPath=$current_location/InferenceScripts/

if [[ "$select_model" == *"yolov5"* ]]; then
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV5/weights/$select_model.pt
    fi
    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
    fi

    cd "$current_location/YoloModels/YoloV5/"
    python3 val.py \
        --data $datasetPath \
        --weights $weights \
        --conf-thres $confThr \
        --iou-thres $iouThr\
        --batch-size $batchSize \
        --project $experimetsPath/YoloV5/eval \
        --name exp \

    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    else
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    fi
elif [[ "$select_model" == *"yolov6"* ]]; then
    nc=$(yq e '.nc' $datasetPath)
    names=$(yq e '.names' $datasetPath)
    export NC_PARAMETER="$nc"
    export NAMES_PARAMETER="$names"
    source_file1="$inferenceScriptsPath/evaler.py"
    destination_directory1="$current_location/YoloModels/YoloV6/yolov6/core/"
    cp "$source_file1" "$destination_directory1"
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV6/weights/$select_model.pt
    fi
    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
    fi

    cd "$current_location/YoloModels/YoloV6/"
    python3 eval.py \
        --data $datasetPath \
        --batch-size $batchSize \
        --weights $weights \
        --task val \
        --conf-thres $confThr \
        --iou-thres $iouThr\
        --save_dir  $experimetsPath/YoloV6/eval/eval \
        --name exp \
        --do_coco_metric True --do_pr_metric True --plot_curve True --plot_confusion_matrix

    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    else
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    fi

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
    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
    fi

    cd "$current_location/YoloModels/YoloV7/"
    python3 test.py \
        --data $datasetPath \
        --batch-size $batchSize \
        --img $imgSize \
        --weights $weights \
        --conf-thres $confThr \
        --iou-thres $iouThr \
        --project $experimetsPath/YoloV7/eval \
        --name exp \
        --iou $iouThr
#python test.py --data data/coco.yaml --img 640
#--batch 32 --conf 0.001 --iou 0.65 --device 0 --weights yolov7.pt --name yolov7_640_val

    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    else
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    fi

elif [[ "$select_model" == *"yolov8"* ]]; then
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV8/weights/$select_model.pt
    fi
    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
    fi

    yolo \
        task=detect \
        mode=val \
        model=$weights \
        project=$experimetsPath/YoloV8/eval \
        name=exp \
        data=$datasetPath \
        imgsz=$imgSize \
        conf=$confThr \
        iou=$iouThr

    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    else
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    fi

elif [[ "$select_model" == *"yolov9"* && "$select_model" != *"converted"* ]]; then
    cd "$experimetsPath/YoloV9/weights/"
    weights_url="https://github.com/WongKinYiu/yolov9/releases/download/v0.1/$select_model.pt"
    if [ -f "$select_model.pt" ]; then
        echo "Weights $select_model.pt exists..."
    else
        echo "Download weights $select_model.pt..."
        curl -L -o "$select_model.pt" "$weights_url"
    fi
    if [ -z "$weights" ]; then
        weights=$experimetsPath/YoloV8/weights/$select_model.pt
    fi
    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
    fi
    cd "$current_location/YoloModels/YoloV9/"
    python3 val_dual.py \
        --data $datasetPath \
        --batch-size $batchSize \
        --weights $experimetsPath/YoloV9/weights/$select_model.pt \
        --conf-thres $confThr \
        --iou-thres $iouThr \
        --project $experimetsPath/YoloV9/eval \
        --name exp \
        --img $imgSize \

    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    else
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    fi

elif [[ "$select_model" == *"gelan"* || "$select_model" == *"converted"* ]]; then
    cd "$experimetsPath/YoloV9/weightsGelan/"
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
    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
    fi
    cd "$current_location/YoloModels/YoloV9/"
    python3 val.py \
        --data $datasetPath \
        --batch-size $batchSize \
        --weights $experimetsPath/YoloV9/weights/$select_model.pt \
        --conf-thres $confThr \
        --iou-thr $iouThr\
        --project $experimetsPath/YoloV9/evalGelan \
        --name exp \
        --img $imgSize \

    if [[ "$testSplit" == *"test"* ]]; then
        evalSelect
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    else
        echo "Evaluation performed on <<$testSplit>> images from $datasetPath dataset."
    fi

else
    echo "Invalid model. Please provide either 'yolov5', 'yolov6', 'yolov7', 'yolov8', 'yolov9', 'gelan' or 'yolonas'."
fi

