from . import student
from . import graduation
from . import subject
from . import teacher


routes = [
    graduation.router,
    student.router,
    subject.router,
    teacher.router
]
