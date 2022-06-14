from fastapi import FastAPI
from .version import version

app = FastAPI()


@app.get("/")
async def status():
    return {
        "ok": True,
        "version": version
    }
