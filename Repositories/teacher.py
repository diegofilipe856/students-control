from sqlalchemy.orm import Session

from Domain.Models.teacher import TeacherModel


def create_teacher(db: Session, teacher_data: TeacherModel):
    db.add(teacher_data)
    db.commit()
    db.refresh(teacher_data)
    return {'msg': "Professor criado com sucesso! ;)"}

