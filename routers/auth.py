from fastapi import APIRouter, Depends
from typing import Annotated
from schemas.publishers import CreatePublisherRequest
from starlette import status
from database.database import SessionLocal
from database.models import Publishers
from passlib.context import CryptContext
from sqlalchemy.orm import Session



router = APIRouter(prefix="/auth", tags=["auth"])

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_publisher(db: db_dependency, create_publicher_request: CreatePublisherRequest):
    create_publisher_model = Publishers(
        email=create_publicher_request.email,
        username=create_publicher_request.username,
        first_name=create_publicher_request.first_name,
        last_name=create_publicher_request.last_name,
        hashed_password=bcrypt_context.hash(create_publicher_request.password),
        is_active=True
    )

    db.add(create_publisher_model)
    db.commit()
    