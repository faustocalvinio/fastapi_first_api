from pydantic import BaseModel


class Car(BaseModel):
    name: str
    price: int
