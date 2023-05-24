from sqlalchemy.orm import Session

from Domain.Models.student import Student
from Repositories.student import get_students, create_studentdb, get_student
'''from domain.models.item import Item
from domain.schemas.user import UserCreate
from domain.schemas.item import ItemCreate
from repositories import user as user_repository
'''


def get_all_students(db):
    return get_students(db)


def get_student_by_id(student_id, db: Session):
    return get_student(db, student_id)


def create_student(db: Session, student_data):
    return create_studentdb(db, student_data)


def modify_student_graduation(db: Session, student_id):
    return {'msg': '(Em construção) Aqui você modificará a graduação de um aluno! :D'}



