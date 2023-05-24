from pydantic import Field
from Domain.Schemas.generic import GenericModel


class StudentBase(GenericModel):
    id: str = Field(title='Student ID: ', example='UUID')


class Student(StudentBase):
    name: str = Field(title='Nome do estudante: ', example='Douglas')
    cpf: str = Field(title='CPF: ', example='123.456.789-01')
    age: int = Field(title='Idade: ', example='19')
    rg: str = Field(title='RG: ', example='12.345.678')
    dispatching_agency: str = Field(title='Órgão expeditor: ', example='SDS')
    birthday: str = Field(title='Data de aniversário: ', example='15/01')
    graduation_id: str = Field(title='ID da graduação: ', example='UUID')


class EnrollStudent(GenericModel):
    studentCpf: str = Field(title='Digite o CPF do estudante: ', example='000.000.000.-00')
    subjectCode: str = Field(title='Digite o código da disciplina que o estudante será matriculado: ', example='EQUI000')


class EnrollStudentdb(GenericModel):
    studentId: str
    subjectId: str
