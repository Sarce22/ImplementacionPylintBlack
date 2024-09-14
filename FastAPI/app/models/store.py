from pydantic import BaseModel


class Store(BaseModel):
    id: str
    nombre: str
    direccion: str