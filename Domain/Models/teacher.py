from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from Domain.Models.generic import GenericBase


class TeacherModel(GenericBase):
    __tablename__ = "Teachers"

    id = Column(String, primary_key=True)
    name = Column(String)
    cpf = Column(String, unique=True)
    titulation = Column(String)

    Subject = relationship("Subject", back_populates="TeacherModel")
    Graduation = relationship("Graduation", back_populates="TeacherModel")

