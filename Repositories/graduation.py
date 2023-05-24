from sqlalchemy.orm import Session

from Domain.Models.graduation import Graduation


def create_graduation(db: Session, graduation_data: Graduation):
    db.add(graduation_data)
    db.commit()
    db.refresh(graduation_data)
    return {'msg': "Curso criado com sucesso! ;)"}
