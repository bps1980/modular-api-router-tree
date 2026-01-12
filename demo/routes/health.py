health_router = {
    "prefix": "/health",
    "routes": [
        {"method": "GET", "path": "/", "handler": "health_check"},
    ]
}

def health_check():
    return {"status": "ok"}
