#!/bin/bash

# Set your desired image name
IMAGE_NAME="inception"

# Stop and remove any existing container with the same name
docker rm -f $IMAGE_NAME 2>/dev/null || true

# Build the Docker image
docker build -t $IMAGE_NAME .

# Start the container in detached mode
docker run -itd --name $IMAGE_NAME -v "$(pwd):/app" $IMAGE_NAME bash

# Run the unit tests inside the container and save output to file
docker exec $IMAGE_NAME pytest 2>&1 | tee test_output

# Copy the test output to the clipboard and print to screen

cat test_output | python3 -c "import sys, pyperclip; pyperclip.copy(sys.stdin.read())" && echo "✓ $(( $(cat test_output | wc -l) - 1 )) lines of test output were copied to the clipboard."

# Remove the output file
rm -f test_output

# Stop and remove the container
docker stop $IMAGE_NAME && docker rm $IMAGE_NAME
