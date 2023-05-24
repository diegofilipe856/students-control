from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Domain.Models.generic import GenericBase


class Subject(GenericBase):
    __tablename__ = "Subjects"

    id = Column(String, primary_key=True, nullable=False)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    teacher_id = Column(String, ForeignKey("Teachers.id"), nullable=False)
    description = Column(String, default=None)

    Student = relationship("Student", secondary='Student_subject', back_populates="Subject")
    TeacherModel = relationship("TeacherModel", back_populates="Subject")
#    student = relationship("Aluno", secondary='ALUNOS_DISCIPLINAS', back_populates="classes")