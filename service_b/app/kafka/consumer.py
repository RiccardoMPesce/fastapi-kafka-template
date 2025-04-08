import asyncio
import json
import os
from aiokafka import AIOKafkaConsumer
from ..models.models import MessageIn
from ..config import settings
import logging

# Configure logger
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

async def process_message(message):
    """Process incoming messages from Kafka"""
    try:
        value = json.loads(message.value.decode())
        message_obj = MessageIn(**value)
        logger.info(f"Received message: {message_obj}")
        # Add your business logic to handle the message here
    except Exception as e:
        logger.error(f"Error processing message: {e}")

async def start_consumer():
    """Start the Kafka consumer"""
    consumer = AIOKafkaConsumer(
        settings.CONSUMER_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id=settings.KAFKA_CONSUMER_GROUP,
        auto_offset_reset="earliest",
    )
    
    try:
        await consumer.start()
        logger.info(f"Started consumer, listening to topic {settings.CONSUMER_TOPIC}")
        
        async for msg in consumer:
            await process_message(msg)
    finally:
        await consumer.stop()