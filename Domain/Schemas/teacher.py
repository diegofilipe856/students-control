from sqlalchemy import Boolean, Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from Domain.Schemas.generic import GenericModel


class BaseTeacher(GenericModel):
    id: str


class Teacher(BaseTeacher):
    name: str
    cpf: str
    titulation: str

