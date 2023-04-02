#!/bin/bash

# Set your desired image name
IMAGE_NAME="inception"

# Stop and remove any existing container with the same name
docker rm -f $IMAGE_NAME 2>/dev/null || true

# Build the Docker image
docker build -t $IMAGE_NAME .

# Run a container with an interactive shell in the /app directory
docker run -it --rm -v "$(pwd):/app" -w /app $IMAGE_NAME /bin/bash

