from fastapi import APIRouter
from .highlight_message import highlight_message_router

message_router = APIRouter()
message_router.include_router(highlight_message_router)
