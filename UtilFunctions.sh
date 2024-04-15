#!/bin/bash

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