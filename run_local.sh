#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Build and run the Docker containers
docker-compose up --build
