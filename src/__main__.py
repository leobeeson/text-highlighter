import uvicorn


def start_server():
    uvicorn.run(
        "src.app:app",
        host="127.0.0.1",
        port=5678,
        log_level="info",
        reload=True,
    )


if __name__ == '__main__':
    start_server()
