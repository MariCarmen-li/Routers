from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

class Shoe(BaseModel):
    idshoes: int
    type: str
    num: float

shoes_list = [
    Shoe(idshoes=1, type="Tennis", num=3.5),
    Shoe(idshoes=2, type="Formal", num=7.0),
    Shoe(idshoes=3, type="Bota", num=8.5),
    Shoe(idshoes=4, type="Sandalia", num=5.0),
    Shoe(idshoes=5, type="Chanclas", num=4.0)
]

routerShoes = APIRouter()

@routerShoes.get("/6/", status_code=status.HTTP_200_OK)
async def shoesclass():
    return shoes_list

@routerShoes.get("/6/{id}", status_code=status.HTTP_200_OK)
async def shoesclass(id: int):
    shoes = filter(lambda shoe: shoe.idshoes == id, shoes_list)
    try:
        return list(shoes)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)