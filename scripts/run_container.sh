#!/bin/bash

IMAGE_TAG=${IMAGE_TAG:-facial-age-estimation-dev}
CONTAINER_NAME=${IMAGE_TAG}-container

PORT=${PORT:-4321}

DATA_DIR=${DATA_DIR:-/hadatasets/facial-age-estimation}
WORK_DIR=${WORK_DIR:-$PWD}

echo "Datasets directory: $DATA_DIR"
echo "Work directory: $WORK_DIR"

exec docker run \
    --gpus all \
    --shm-size=8g \
    -p "$PORT":"$PORT" \
    -v "$WORK_DIR":/work/notebooks \
    -v "$DATA_DIR":/datasets \
    -t "$IMAGE_TAG" \
    --name "$CONTAINER_NAME"