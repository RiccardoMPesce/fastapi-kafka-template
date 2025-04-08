import asyncio
import json
import os
from aiokafka import AIOKafkaConsumer
from ..models.models import MessageIn

# Get Kafka bootstrap servers from environment variable or use default
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
# Similar to Service A but consumes from "service-a-events" topic
CONSUMER_TOPIC = os.getenv("CONSUMER_TOPIC", "service-a-events")

async def process_message(message):
    """Process incoming messages from Kafka"""
    try:
        value = json.loads(message.value.decode())
        message_obj = MessageIn(**value)
        print(f"Service B received: {message_obj}")
        # Add your business logic to handle the message here
        # For example, process the request and respond back
    except Exception as e:
        print(f"Error processing message: {e}")

async def start_consumer():
    """Start the Kafka consumer"""
    consumer = AIOKafkaConsumer(
        CONSUMER_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="service-a-group",
        auto_offset_reset="earliest",
    )
    
    try:
        await consumer.start()
        print(f"Started consumer, listening to topic {CONSUMER_TOPIC}")
        
        async for msg in consumer:
            await process_message(msg)
    finally:
        await consumer.stop()