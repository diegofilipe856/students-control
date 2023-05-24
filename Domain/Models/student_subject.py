from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from Domain.Models.generic import GenericBase


class StudentSubject(GenericBase):
    __tablename__ = 'Student_subject'

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)

    student_id = Column(String, ForeignKey("Students.id"), nullable=False)
    subject_id = Column(String, ForeignKey("Subjects.id"), nullable=False)

    __table_args__ = (UniqueConstraint("student_id", "subject_id"),)
