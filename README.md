# fastapi-kafka-template
Template to develop FastAPI based microservices communicating through Kafka

## Setup and Run Locally

To set up and run the project locally, follow these steps:

1. **Create a virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the project using Docker:**
   ```bash
   ./run_local.sh
   ```

This command will activate the virtual environment, build the Docker containers, and start the services.
