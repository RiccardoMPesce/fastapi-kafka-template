import json
import os
from aiokafka import AIOKafkaProducer

# Get Kafka bootstrap servers from environment variable or use default
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
PRODUCER_TOPIC = os.getenv("PRODUCER_TOPIC", "service-a-events")

class KafkaProducer:
    producer = None

    @classmethod
    async def get_producer(cls):
        if cls.producer is None:
            cls.producer = AIOKafkaProducer(
                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS
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
    producer = await KafkaProducer.get_producer()
    value = json.dumps(message_dict).encode()
    await producer.send_and_wait(PRODUCER_TOPIC, value)
    print(f"Message sent to topic {PRODUCER_TOPIC}: {message_dict}")