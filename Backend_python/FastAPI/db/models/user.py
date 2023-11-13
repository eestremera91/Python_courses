# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=20480

### User model ###

from pydantic import BaseModel
from typing import Optional  # Así si lo tengo en versión 3.9


class User(BaseModel):
#   id: str | None   # lo pongo como un string para que sea grande y opcional que puede que le llegue o no como dato
    id: Optional[str]   # Así si lo tengo en versión 3.9
    username: str
    email: str
