from dto.message_dto import MessageDTO

messages_router = {
    "prefix": "/messages",
    "routes": [
        {"method": "GET", "path": "/", "handler": "get_messages"},
        {"method": "POST", "path": "/", "handler": "send_message"},
    ]
}

def get_messages():
    return [{"id": 1, "message": "Hello world"}]

def send_message(payload: MessageDTO):
    return {"status": "sent", "message": payload.to_dict()}
