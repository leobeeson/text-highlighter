from fastapi import APIRouter
from src.version import version

status_router = APIRouter()


@status_router.get("/")
def status():
    return {
        "ok": True,
        "version": version
    }
