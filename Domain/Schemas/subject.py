from pydantic import Field
from Domain.Schemas.generic import GenericModel


class BaseSubject(GenericModel):
    id: str
    code: str
    name: str
    teacher_id: str


class Subject(BaseSubject):
    description: str
