from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Config.database import get_session
from Domain.Schemas.student import Student
from Services import student as student_service

router = APIRouter()


@router.get(
    "/student",
    summary="Get all students data.",
    response_model=dict,
    tags=["Student"],
)
def get_students(db: Session = Depends(get_session)):
    return student_service.get_all_students(db)


@router.get(
    "/student/{student_id}",
    summary="Get a student by the id",
    response_model=dict,
    tags=["Student"],
)
def get_student_by_id(student_id: str, db: Session = Depends(get_session)):
    return student_service.get_student_by_id(student_id, db)


@router.post(
    "/student",
    summary="Create a new student",
    response_model=dict,
    tags=["Student"],
)
def create_student(student_data: Student, db: Session = Depends(get_session)):
    return student_service.create_student(db, student_data)


@router.put(
    "/{student_id}/change-graduation",
    summary='Change the graduation of a student',
    response_model=dict,
    tags=["Student"],
)
def modify_student_graduation(student_id, db: Session = Depends(get_session)):
    return student_service.modify_student_graduation(db, student_id)
