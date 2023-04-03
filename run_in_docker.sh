#!/bin/bash

# Set your desired image name
IMAGE_NAME="inception"

# Stop and remove any existing container with the same name
docker rm -f $IMAGE_NAME 2>/dev/null || true

# Build the Docker image
docker build -t $IMAGE_NAME .

# Start the container in detached mode
docker run -it --name $IMAGE_NAME $IMAGE_NAME bash

# Stop and remove the container when you exit the bash prompt
docker stop $IMAGE_NAME && docker rm $IMAGE_NAME

