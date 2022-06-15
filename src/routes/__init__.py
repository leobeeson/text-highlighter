from fastapi import APIRouter
from .message import message_router
from .status import status_router

router = APIRouter()
router.include_router(status_router)
router.include_router(message_router, prefix="/message")
