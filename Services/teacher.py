from sqlalchemy.orm import Session
from Domain.Models.teacher import TeacherModel
from Domain.Schemas.teacher import Teacher
from Repositories.teacher import create_teacher


def create_teacher_service(db: Session, teacher_data: Teacher):
    db_teacher = TeacherModel(id=teacher_data.id, name=teacher_data.name, cpf=teacher_data.cpf, titulation=teacher_data.titulation)
    return create_teacher(db, db_teacher)