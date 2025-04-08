import os
from typing import Any, Dict, Optional
from pydantic_settings import BaseSettings
from pydantic import field_validator
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    """Application settings"""
    
    # Service info
    SERVICE_NAME: str = "service_b"
    API_PORT: int = 8000
    LOG_LEVEL: str = "INFO"
    
    # Kafka settings
    KAFKA_BOOTSTRAP_SERVERS: str = "kafka:9092"
    CONSUMER_TOPIC: str = "service-a-events"
    PRODUCER_TOPIC: str = "service-b-events"
    KAFKA_CONSUMER_GROUP: str = "service-b-group"
    
    # Additional settings
    MAX_RETRY_ATTEMPTS: int = 3
    REQUEST_TIMEOUT_SECONDS: int = 30
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create global settings instance
settings = Settings()