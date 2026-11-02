from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

router = APIRouter(
    prefix="/api/v1/hotels",
    tags=["Hotels"]
)


@router.get("/")
def get_hotels(db: Session = Depends(get_db)):

    return {
        "success": True,
        "message": "Database session connected successfully"
    }