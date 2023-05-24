from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Config.database import get_session
from Domain.Schemas.subject import Subject
from Domain.Schemas.student import EnrollStudent
from Services import subject as subject_service

router = APIRouter()


@router.post(
    "/subject",
    summary='Creates a subject',
    tags=['Subject'],
    response_model=dict,
)
def create_subject(subject_data: Subject, db: Session = Depends(get_session)):
    return subject_service.create_subject(db, subject_data)


@router.post(
    "/subject/enroll",
    summary='Enroll a student in a subject',
    tags=['Subject'],
    response_model=dict,
)
def enroll_student(data: EnrollStudent, db: Session = Depends(get_session)):
    return subject_service.enroll_student(db, data)


@router.delete(
    "/subject/unenroll",
    summary='Unenroll a student of a subject',
    tags=['Subject'],
    response_model=dict,
)
def unenroll_student(data: EnrollStudent, db: Session = Depends(get_session)):
    return subject_service.unenroll_student(db, data)


@router.get(
    "/subject/{subject_id}",
    summary='Show students enrolled in a subject',
    tags=['Subject'],
    response_model=dict,
)
def students_in_subjects(subject: str, db: Session = Depends(get_session)):
    return subject_service.students_in_subject(db, subject)


@router.post(
    "/subject/ranking",
    summary="Show a ranking of subjects",
    response_model=dict,
    tags=["Subject"],
)
def ranking_subjects(db: Session = Depends(get_session)):
    return subject_service.ranking_of_subjects(db)
