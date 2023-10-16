from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

class Computer(BaseModel):
    idcomputer: int
    marca: str
    RAM: int

computers_list = [
    Computer(idcomputer=1, marca="HP", RAM=8),
    Computer(idcomputer=2, marca="LENOVO", RAM=4),
    Computer(idcomputer=3, marca="ASUS", RAM=12),
    Computer(idcomputer=4, marca="TOSHIBA", RAM=16),
    Computer(idcomputer=5, marca="HP", RAM=8)
]

routerComputers = APIRouter()

@routerComputers.get("/7/", status_code=status.HTTP_200_OK)
async def computersclass():
    return computers_list

@routerComputers.get("/7/{id}", status_code=status.HTTP_200_OK)
async def computersclass(id: int):
    computers = filter(lambda computer: computer.idcomputer == id, computers_list)
    try:
        return list(computers)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)