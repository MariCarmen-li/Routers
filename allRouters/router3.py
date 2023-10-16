from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

class Animal (BaseModel):
    idanimal: int
    name: str
    sex: str

animals_list = [
    Animal(idanimal=1, name="Lion", sex="F"),
    Animal(idanimal=2, name="Tiger", sex="M"),
    Animal(idanimal=3, name="Horse", sex="F"),
    Animal(idanimal=4, name="Cat", sex="F"),
    Animal(idanimal=5, name="Dog", sex="M"),
]

routerAnimals = APIRouter()

@routerAnimals.get("/3/", status_code=status.HTTP_200_OK)
async def animalsclass():
    return animals_list

@routerAnimals.get("/3/{id}")
async def animalsclass(id: int):
    animals = filter(lambda animal: animal.idanimal == id, animals_list)
    try:
        return list(animals)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)