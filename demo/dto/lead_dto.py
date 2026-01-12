class LeadDTO:
    def __init__(self, name: str, source: str):
        self.name = name
        self.source = source

    def to_dict(self):
        return {
            "name": self.name,
            "source": self.source
        }
