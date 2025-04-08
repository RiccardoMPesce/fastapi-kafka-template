from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class MessageIn(BaseModel):
    message_id: str
    event_type: str
    data: Dict[str, Any]
    timestamp: Optional[datetime] = None

class MessageOut(BaseModel):
    message_id: str
    event_type: str
    data: Dict[str, Any]
    timestamp: datetime = datetime.now()