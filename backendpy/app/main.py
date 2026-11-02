from fastapi import FastAPI

from app.core.config import settings
from app.api.auth import router as auth_router
from sqlalchemy import text
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Hotel SaaS Management API"
)


app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Welcome to Hotel SaaS API"
    }


@app.get("/health")
def health():
    return {
        "success": True,
        "status": "API is running"
    }


@app.get("/health/database")
def database_health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "success": True,
            "message": "PostgreSQL connection successful"
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }