# FastAPI Microservices Template with Kafka

This project provides a template for building microservices using Python FastAPI that communicate via Apache Kafka. It's designed to help you quickly bootstrap a microservices architecture with modern tooling and best practices.

## 📋 Features

- **FastAPI Microservices**: High-performance REST APIs built with FastAPI
- **Kafka Communication**: Asynchronous messaging between services using Kafka
- **Docker Containerization**: Containerized deployment with Docker and Docker Compose
- **Environment Configuration**: Flexible environment management for different deployment scenarios
- **Structured Logging**: Consistent logging across all services
- **Health Checks**: Endpoints for monitoring service health
- **Scalable Architecture**: Designed to easily add new microservices to the ecosystem

## 🏗️ Architecture

The template consists of two example microservices that communicate via Kafka:

- **Service A**: Sends messages to Service B
- **Service B**: Receives messages from Service A and processes them

The services are completely decoupled and only communicate through Kafka topics, demonstrating how to build resilient distributed systems.

## 📂 Project Structure

```
microservices-kafka-template/
├── docker-compose.yml
├── requirements.txt
├── run_local_dev.sh
├── .gitignore
├── README.md
├── service_a/
│   ├── Dockerfile
│   ├── .env
│   ├── .env.dev
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── kafka/
│   │   │   ├── __init__.py
│   │   │   ├── consumer.py
│   │   │   └── producer.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   └── api/
│   │       ├── __init__.py
│   │       └── endpoints.py
├── service_b/
│   ├── Dockerfile
│   ├── .env
│   ├── .env.dev
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── kafka/
│   │   │   ├── __init__.py
│   │   │   ├── consumer.py
│   │   │   └── producer.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   └── api/
│   │       ├── __init__.py
│   │       └── endpoints.py
```

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.9+](https://www.python.org/downloads/) (for local development)

### Running with Docker

The easiest way to run the application is with Docker Compose:

```bash
# Start all services
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop all services
docker-compose down
```

### Running Locally for Development

For local development, you can use the provided script (assumes you have Kafka running locally):

```bash
# Make script executable
chmod +x run_local_dev.sh

# Run the script
./run_local_dev.sh
```

Or run services individually:

```bash
# Service A
cd service_a
cp .env.dev .env
uvicorn app.main:app --reload --port 8000

# Service B (in another terminal)
cd service_b
cp .env.dev .env
uvicorn app.main:app --reload --port 8001
```

## 🔍 Testing the Services

### Health Checks

```bash
# Check Service A health
curl http://localhost:8000/health/

# Check Service B health
curl http://localhost:8001/health/
```

### Send a Message

```bash
# Send a message from Service A to Service B
curl -X POST http://localhost:8000/send-message/ \
  -H "Content-Type: application/json" \
  -d '{"action": "test", "value": "Hello from Service A"}'
```

## 🔧 Configuration

Each service has its own environment configuration:

- `.env` - Used in production and Docker environments
- `.env.dev` - Used for local development

Key configuration parameters:

| Parameter | Description |
|-----------|-------------|
| SERVICE_NAME | Name of the service |
| API_PORT | Port the FastAPI service runs on |
| LOG_LEVEL | Logging level (DEBUG, INFO, WARNING, ERROR) |
| KAFKA_BOOTSTRAP_SERVERS | Kafka broker address |
| CONSUMER_TOPIC | Topic from which the service consumes messages |
| PRODUCER_TOPIC | Topic to which the service produces messages |
| KAFKA_CONSUMER_GROUP | Consumer group ID for the service |
| MAX_RETRY_ATTEMPTS | Number of retry attempts for failed operations |
| REQUEST_TIMEOUT_SECONDS | Timeout for external requests |

## 📚 API Documentation

When the services are running, you can access the auto-generated API documentation:

- Service A: http://localhost:8000/docs
- Service B: http://localhost:8001/docs

## 🌱 Extending the Template

### Adding a New Service

1. Copy an existing service directory (e.g., `service_a`) to a new directory (e.g., `service_c`)
2. Update the `.env` and `.env.dev` files with appropriate values
3. Modify the Kafka topics and message handling logic
4. Add the new service to `docker-compose.yml`

### Implementing New Features

The template is designed to be modular, making it easy to add new features:

- Add new API endpoints in the `api/endpoints.py` file
- Define new models in the `models/models.py` file
- Implement new Kafka producers and consumers as needed

## 🔐 Security Considerations

- Environment variables contain sensitive information - never commit `.env` files
- Add proper authentication and authorization for production deployments
- Implement network security policies in production environments
- Consider using TLS for Kafka communication in production

## 📈 Monitoring and Observability

For production environments, consider adding:

- Prometheus metrics for service monitoring
- Distributed tracing with OpenTelemetry
- Centralized logging with ELK stack or similar
- Alerting based on service health and performance

## 🧪 Testing

To implement testing:

- Create unit tests for business logic
- Create integration tests for API endpoints
- Create end-to-end tests for service communication

## 📄 License

[MIT](LICENSE)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For any questions or issues, please open an issue in the repository.

---

Happy coding! 🚀