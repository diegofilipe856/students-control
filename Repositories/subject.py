from sqlalchemy.orm import Session

from Domain.Models.subject import Subject
from Domain.Models.student import Student
from Domain.Models.student_subject import StudentSubject


def create_subjectdb(db, db_subject):
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return {"msg": "Disciplina criada com sucesso!"}


def enroll_studentdb(db, db_student_subject):
    db.add(db_student_subject)
    db.commit()
    db.refresh(db_student_subject)
    db.close()
    return {'msg': 'Estudante matriculado com sucesso! ;)'}


def unenroll_studentdb(db, db_student_subject):
    db.query(StudentSubject).filter(StudentSubject.student_id == db_student_subject.student_id).filter(StudentSubject.subject_id == db_student_subject.subject_id).delete()
    db.commit()
    return {'msg': "Estudante desmatriculado com sucesso! ;)"}


def ranking_subjectsdb(db):
    subjects = db.query(Subject.id).all()
    array_of_subjects = []
    for subject in subjects:
        subject = subject[0]
        code = db.query(Subject.code).filter(Subject.id == subject).first()
        code = code[0]
        temp_dict = {}
        temp_dict['code'] = code
        number_of_students = db.query(StudentSubject.student_id).filter(StudentSubject.subject_id == subject).all()
        print('-'*5)
        print(number_of_students)
        print('-'*5)
        temp_dict["number_of_students"] = len(number_of_students)
        array_of_subjects.append(temp_dict)
    array_of_subjects = sorted(array_of_subjects, key=lambda x: x['number_of_students'], reverse=True)
    return {'msg': 'Aqui você verá um ranking de disciplinas! :D',
            'prompt': array_of_subjects}
