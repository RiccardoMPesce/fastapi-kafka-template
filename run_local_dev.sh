#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Set environment to development
export ENV_FILE=.env.dev

echo "Starting services in development mode..."

# Start Service A
cd service_a
cp .env.dev .env
echo "Starting Service A on port 8000..."
uvicorn app.main:app --reload --port 8000 &
SERVICE_A_PID=$!

# Start Service B
cd ../service_b
cp .env.dev .env
echo "Starting Service B on port 8001..."
uvicorn app.main:app --reload --port 8001 &
SERVICE_B_PID=$!

# Wait for termination
echo "Services started. Press CTRL+C to stop."
trap "kill $SERVICE_A_PID $SERVICE_B_PID; exit" INT TERM
wait