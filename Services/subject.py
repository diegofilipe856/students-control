from sqlalchemy.orm import Session
import Domain.Models.student
import Domain.Models.subject
import Domain.Models.teacher
from Domain.Schemas.teacher import Teacher
from Domain.Schemas.subject import Subject
from Domain.Models.student_subject import StudentSubject
from Repositories.subject import *


def create_subject(db: Session, subject_data):
    db_subject = Subject(id=subject_data.id, code=subject_data.code, name=subject_data.name, teacher_id=subject_data.teacher_id, description=subject_data.description)
    verify_teacher = db.query(Domain.Models.teacher.TeacherModel).filter(db_subject.teacher_id == Domain.Models.teacher.TeacherModel.id).first()
    if verify_teacher:
        return create_subjectdb(db, db_subject)
    else:
        return {'erro': "Professor não encontrado! :("}


def enroll_student(db: Session, data):
    student_cpf = data.studentCpf
    subject_code = data.subjectCode
    student = db.query(Student.id).filter(student_cpf == Domain.Models.student.Student.cpf).first()
    subject = db.query(Subject.id).filter(subject_code == Domain.Models.subject.Subject.code).first()
    if student is not None and subject is not None:
        student = str(student[0])
        subject = str(subject[0])
        db_student_subject = StudentSubject(student_id=student, subject_id=subject)
        return enroll_studentdb(db, db_student_subject)
    else:
        return {'erro': "Erro! O aluno e/ou disciplina não existe(m)."}


def unenroll_student(db: Session, data):
    student_cpf = data.studentCpf
    subject_code = data.subjectCode
    student = db.query(Student.id).filter(student_cpf == Domain.Models.student.Student.cpf).first()
    subject = db.query(Subject.id).filter(subject_code == Domain.Models.subject.Subject.code).first()

    if student is not None and subject is not None:
        student = str(student[0])
        subject = str(subject[0])
        db_student_subject = StudentSubject(student_id=student, subject_id=subject)
        return unenroll_studentdb(db, db_student_subject)
    else:
        return {'erro': "Erro! O aluno e/ou disciplina não existe(m)."}


def students_in_subject(db: Session, subject):
    subject_id = db.query(Domain.Models.subject.Subject.id).filter(Domain.Models.subject.Subject.code == subject).first()
    subject_id = subject_id[0]
    all_students = db.query(StudentSubject.student_id). filter(StudentSubject.subject_id == subject_id).all()
    all_students = all_students
    list_of_names = []
    for i in all_students:
        i = i[0]
        temp_name = db.query(Domain.Models.student.Student.name). filter(Domain.Models.student.Student.id == i).first()
        list_of_names.append(temp_name)

    return {'msg': "Aqui você verá os estudantes matriculados numa disciplina! :D",
            'prompt': list_of_names}


def ranking_of_subjects(db):
    return ranking_subjectsdb(db)