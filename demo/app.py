from routes.leads import leads_router
from routes.messages import messages_router
from routes.health import health_router

# This is a placeholder for a real framework (FastAPI, Flask, Actix, etc.)
# The goal is to show structure, not functionality.

class App:
    def __init__(self):
        self.routes = []

    def include_router(self, router):
        self.routes.append(router)

app = App()

# Register modular routers
app.include_router(leads_router)
app.include_router(messages_router)
app.include_router(health_router)

if __name__ == "__main__":
    print("Registered routes:")
    for r in app.routes:
        print(f"- {r['prefix']}")
