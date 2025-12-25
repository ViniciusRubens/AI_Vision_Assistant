#!/bin/bash

# Image name
IMAGE_NAME="vilt-project"

echo "Starting build for Docker image: $IMAGE_NAME..."

docker build -t $IMAGE_NAME .

echo "Build finished successfully!"