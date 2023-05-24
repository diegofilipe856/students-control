from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Config.database import get_session
from Domain.Schemas.graduation import Graduation
from Services import graduation as graduation_service

router = APIRouter()


@router.post(
    "/graduation",
    summary="Create a new graduation",
    response_model=dict,
    tags=['Graduation']
)
def create_graduation(graduation_data: Graduation, db: Session = Depends(get_session)):
    return graduation_service.create_graduation(db, graduation_data)
