from Domain.Schemas.generic import GenericModel


class BaseGraduation(GenericModel):
    id: str
    name: str


class Graduation(BaseGraduation):
    date_of_creation: str
    coordinator: str
    building_name: str
