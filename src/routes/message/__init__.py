from fastapi import APIRouter
from .redact_message import redact_message_router

message_router = APIRouter()
message_router.include_router(redact_message_router)
