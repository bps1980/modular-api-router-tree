from dto.lead_dto import LeadDTO

leads_router = {
    "prefix": "/leads",
    "routes": [
        {"method": "GET", "path": "/", "handler": "get_leads"},
        {"method": "POST", "path": "/", "handler": "create_lead"},
    ]
}

def get_leads():
    return [{"id": 1, "name": "Example Lead"}]

def create_lead(payload: LeadDTO):
    return {"status": "created", "lead": payload.to_dict()}
