class MessageDTO:
    def __init__(self, lead_id: int, content: str):
        self.lead_id = lead_id
        self.content = content

    def to_dict(self):
        return {
            "lead_id": self.lead_id,
            "content": self.content
        }
