from Config.database import engine
from Domain.Models.generic import GenericBase

from Domain.Models import (
    graduation,
    student,
    subject,
    teacher,
    student_subject
)

GenericBase.metadata.create_all(bind=engine)
