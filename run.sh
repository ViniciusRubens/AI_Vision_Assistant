#!/bin/bash

# Configs
IMAGE_NAME="vilt-project"
CONTAINER_NAME="vilt-web-final"
HOST_PORT=3000
CONTAINER_PORT=3000

echo "Cleaning old containers..."

docker stop $CONTAINER_NAME 2>/dev/null || true
docker rm $CONTAINER_NAME 2>/dev/null || true

echo "Starting container in port $HOST_PORT..."

# Run container
docker run -d \
    --name $CONTAINER_NAME \
    -p $HOST_PORT:$CONTAINER_PORT \
    $IMAGE_NAME

echo "----------------------------------------------------"
echo "API and Interface ready!"
echo "Acess: http://localhost:$HOST_PORT"
echo "----------------------------------------------------"