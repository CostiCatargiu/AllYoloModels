#!/bin/bash

testVideos=$(yq e '.testVideosPath' parameters.yaml)

delete_cache() {
          train=$(yq e '.train' $datasetPath)
          new_path=$(echo "$train" | sed 's/images/labels/')
          new_path=$(echo "$new_path" | sed 's/\/[^/]*$//')
          find "$new_path" -type f -name '*.cache' -delete
}

evalSelect() {
        temp_file="temp.yaml"
        val=$(awk '/val:/ {print $2}' "$datasetPath")
        test=$(awk '/test:/ {print $2}' "$datasetPath")
        awk -v val="$val" -v test="$test" '{sub("val: " val, "val: " test); sub("test: " test, "test: " val)}1' "$datasetPath" > "$temp_file"
        mv "$temp_file" "$datasetPath"
        echo "  optional_param5 (testSplit): default: = $testSplit"

}

downloadCCOCOannotations() {
      folder_path="coco"
      mkdir -p "$folder_path"
      wget -O "$folder_path/data.zip" "images.cocodataset.org/annotations/annotations_trainval2017.zip"
      unzip -q "$folder_path/data.zip" -d "$folder_path"
      rm "$folder_path/data.zip"
      echo "Download and extraction completed."
}

# Function to scan a directory and get the path of a video by its index
#!/bin/bash

# Function to scan a directory and get the path of a video by its index
get_video_path() {
    local directory=$testVideos
    local video_index=$1

    # Create an empty array to store the paths of video files
    declare -a video_list

    # Scan the directory and add video file paths to the array
    while IFS= read -r -d $'\0' file; do
        video_list+=("$file")
    done < <(find "$directory" -type f \( -name "*.mp4" -o -name "*.mkv" \) -print0)

    # Check if video index is provided and valid
    if [[ -z "$video_index" || $video_index -lt 0 || $video_index -ge ${#video_list[@]} ]]; then
        echo "Error: Index out of range or not provided." >&2
        return 1
    else
        # Output only the path of the video at the given index
        echo "${video_list[$video_index]}"
    fi
}



list_videos() {
    local directory=$testVideos

    # Create an empty array to store the paths of video files
    declare -a video_list

    # Scan the directory and add video file paths to the array
    while IFS= read -r -d $'\0' file; do
        video_list+=("$file")
    done < <(find "$directory" -type f \( -name "*.mp4" -o -name "*.mkv" \) -print0)

    # List videos with their index
    echo ":"
    for i in "${!video_list[@]}"; do
        echo "[$i] $(basename "${video_list[$i]}")"
    done
}


