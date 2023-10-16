from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

class User(BaseModel):
    usuarioid: int
    name: str

user_list = [
    User(usuarioid=1, name="Abdiel Jonathan"),
    User(usuarioid=2, name="Pérez Balcón"),
    User(usuarioid=3, name="David López"),
    User(usuarioid=4, name="Maria del Carmen"),
    User(usuarioid=5, name="Luz Rmirez")
]

routerUsuario = APIRouter()

@routerUsuario.get("/2/", status_code=status.HTTP_200_OK)
async def userclass():
    return user_list

@routerUsuario.get("/2/{id}", status_code=status.HTTP_200_OK)
async def userclass(id: int):
    users = filter(lambda user: user.usuarioid == id, user_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)