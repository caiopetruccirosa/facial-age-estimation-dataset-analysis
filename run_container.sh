#!/bin/bash

echo "Notebooks path: $1"
echo "Datasets path: $2"

exec docker run -p 4321:4321 -v "$1":/workspace/notebooks -v "$2":/workspace/datasets -t facial-age-estimation-dataset-analysis
