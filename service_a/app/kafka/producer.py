import json
import os
from aiokafka import AIOKafkaProducer
from ..config import settings
import logging

# Configure logger
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

class KafkaProducer:
    producer = None

    @classmethod
    async def get_producer(cls):
        if cls.producer is None:
            cls.producer = AIOKafkaProducer(
                bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS
            )
            await cls.producer.start()
        return cls.producer

    @classmethod
    async def close_producer(cls):
        if cls.producer is not None:
            await cls.producer.stop()
            cls.producer = None

async def send_message(message_dict):
    """Send a message to Kafka topic"""
    try:
        producer = await KafkaProducer.get_producer()
        value = json.dumps(message_dict).encode()
        await producer.send_and_wait(settings.PRODUCER_TOPIC, value)
        logger.info(f"Message sent to topic {settings.PRODUCER_TOPIC}: {message_dict}")
        return True
    except Exception as e:
        logger.error(f"Failed to send message: {e}")
        return False