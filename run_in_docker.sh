#!/bin/bash

# Set your desired image name
IMAGE_NAME="inception"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Run a container with an interactive shell in the /app directory
docker run -it --rm -v "$(pwd):/app" -w /app $IMAGE_NAME /bin/bash

