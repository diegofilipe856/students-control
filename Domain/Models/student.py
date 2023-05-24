from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Domain.Models.generic import GenericBase


class Student(GenericBase):
    __tablename__ = "Students"

    id = Column(String, primary_key=True)
    name = Column(String)
    cpf = Column(String, unique=True)
    age = Column(Integer, default=None)
    rg = Column(String)
    dispatching_agency = Column(String)
    birthday = Column(String, default=None)
    graduation_id = Column(String, ForeignKey("Graduations.id"))
#   items = relationship("Item", back_populates="owner")

    Subject = relationship("Subject", secondary='Student_subject', back_populates="Student")
    Graduation = relationship("Graduation", back_populates="Student")
