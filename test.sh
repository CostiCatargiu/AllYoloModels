#!/bin/bash

cpu_name=$(cat /proc/cpuinfo | grep "model name" | head -n1 | cut -d ":" -f2 | sed 's/^ *//')
gpu_name=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -n1)
