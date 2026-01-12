A diagram showing:

app.py
   ├── routes/
   │     ├── leads.py
   │     ├── messages.py
   │     └── health.py
   └── dto/
         ├── lead_dto.py
         └── message_dto.py

Arrows show:
- app.py imports routers
- routers import DTOs
- DTOs define request/response structure

The diagram visually represents modular routing and separation of concerns.
