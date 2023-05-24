from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Config.database import get_session
from Domain.Schemas.teacher import Teacher
from Services import teacher as teacher_service

router = APIRouter()


@router.post(
    "/teacher",
    summary='Create a new teacher',
    response_model=dict,
    tags=['Teacher']
)
def create_teacher(teacher_data: Teacher, db: Session = Depends(get_session)):
    return teacher_service.create_teacher_service(db, teacher_data)
