from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.endpoints import create_api
from backend.app.core.config import settings
from backend.app.db.database import init_db

app = FastAPI()

def configure_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.on_event("startup")
async def startup_event():
    await init_db()
    # HUMAN ASSISTANCE NEEDED
    # Additional startup tasks may be required. Please review and add if necessary.

@app.on_event("shutdown")
async def shutdown_event():
    # HUMAN ASSISTANCE NEEDED
    # Implement necessary cleanup tasks, such as closing database connections.
    pass

configure_cors(app)
create_api(app)