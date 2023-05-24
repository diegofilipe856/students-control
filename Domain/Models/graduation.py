from sqlalchemy import Boolean, Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship


from Domain.Models.generic import GenericBase


class GraduationBase(GenericBase):
    __tablename__ = "Graduations"
    id = Column(String, primary_key=True)
    name = Column(String, unique=True)


class Graduation(GraduationBase):
    date_of_creation = Column(String, default=None)
    coordinator = Column(String, ForeignKey("Teachers.id"))
    building_name = Column(String, default=None)

    TeacherModel = relationship("TeacherModel", back_populates="Graduation")
    Student = relationship("Student", back_populates="Graduation")

