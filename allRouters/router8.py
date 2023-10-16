from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

class Lobo (BaseModel):
    idlobo: int
    name: str
    color: str

lobo_list = [
    Lobo(idlobo=1, name="Scot", color="Rojo"),
    Lobo(idlobo=2, name="Allison", color="Blanco"),
    Lobo(idlobo=3, name="Mia", color="Rojo"),
    Lobo(idlobo=4, name="Dereck", color="Azul"),
    Lobo(idlobo=5, name="Styles", color="Amarillo")
]

routerLobo = APIRouter()
@routerLobo.get("/8/", status_code=status.HTTP_200_OK)
async def lobosclass():
    return lobo_list


@routerLobo.get("/8/{id}", status_code=status.HTTP_200_OK)
async def lobosclass(id: int):
    lobos = filter(lambda lobo: lobo.idlobo == id, lobo_list)
    try:
        return list(lobos)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)