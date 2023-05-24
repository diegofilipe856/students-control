from sqlalchemy.orm import Session

from Domain.Models.student import Student


def get_student(db: Session, student_id: str):
    return {'student': db.query(Student).filter(Student.id == student_id).first()}


def get_students(db: Session):
    return {'Students': db.query(Student).all()}


def create_studentdb(db: Session, student_data):
    db_student = Student(id=student_data.id, name=student_data.name, cpf=student_data.cpf, age=student_data.age, rg=student_data.rg, dispatching_agency=student_data.dispatching_agency, birthday=student_data.birthday, graduation_id=student_data.graduation_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {'msg':  "Estudante criado com sucesso! ;)"}
