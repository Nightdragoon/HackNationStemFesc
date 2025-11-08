from pydantic import BaseModel

class UsuarioInsertar(BaseModel):
    nombre: str
    contrasena: str