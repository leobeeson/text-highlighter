from datetime import datetime
from pydantic import BaseModel


class Message(BaseModel):
    recipient_id: str
    sender_id: str
    text: str
    timestamp: datetime
