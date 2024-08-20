#!/bin/bash

# define default values
DEFAULT_IMAGE_TAG="facial-age-dataset-dev"
DEFAULT_DATA_DIR="/hadatasets/facial-age-estimation"

# these variables could be passed as environment variables
IMAGE_TAG=${IMAGE_TAG:-DEFAULT_IMAGE_TAG}
CONTAINER_NAME=${IMAGE_TAG}-container
PORT=${PORT:-4321}
DATA_DIR=${DATA_DIR:-DEFAULT_DATA_DIR}
WORK_DIR=${WORK_DIR:-$PWD}
RAM_SIZE="8g"

exec docker run \
    --gpus all \
    --shm-size=$RAM_SIZE \
    -p "$PORT":"$PORT" \
    -v "$WORK_DIR":/workspace \
    -v "$DATA_DIR":/datasets \
    -d -it --rm \
    --name "$CONTAINER_NAME" \
    "$IMAGE_TAG"
    bash