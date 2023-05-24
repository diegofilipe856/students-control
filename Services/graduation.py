from sqlalchemy.orm import Session
from Domain.Models.graduation import Graduation
from Repositories.graduation import create_graduation


def create_graduation(db: Session, graduation_data):
    db_graduation = Graduation(id=graduation_data.id, name=graduation_data.name, date_of_creation=graduation_data.date_of_creation, coordinator=graduation_data.coordinator, building_name=graduation_data.building_name)
    return create_graduation(db, db_graduation)




