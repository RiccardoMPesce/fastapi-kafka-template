from fastapi import APIRouter, HTTPException
import uuid
from datetime import datetime
from ..models.models import MessageOut
from ..kafka.producer import send_message

router = APIRouter()

@router.post("/send-message/")
async def send_kafka_message(data: dict):
    """API endpoint to send a message to Service B via Kafka"""
    try:
        message = MessageOut(
            message_id=str(uuid.uuid4()),
            event_type="user_action",
            data=data
        )
        await send_message(message.dict())
        return {"status": "Message sent successfully", "message_id": message.message_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send message: {str(e)}")

@router.get("/health/")
async def health_check():
    """Simple health check endpoint"""
    return {"status": "healthy", "service": "Service A"}