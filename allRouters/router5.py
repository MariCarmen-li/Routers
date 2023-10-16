from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

class Trees (BaseModel):
    idtree: int
    name: str
    high: float

trees_list = [
    Trees(idtree=1, name="Evano", high=3.45),
    Trees(idtree=2, name="Roble", high=5.6),
    Trees(idtree=3, name="Arbusto", high=2.0),
    Trees(idtree=4, name="Pino", high=3.6),
    Trees(idtree=5, name="Palmera", high=3.0)
]

routerTrees = APIRouter()

@routerTrees.get("/5/", status_code=status.HTTP_200_OK)
async def treesclass():
    return trees_list

@routerTrees.get("/5/{id}", status_code=status.HTTP_200_OK)
async def treesclass(id: int):
    trees = filter(lambda tree: tree.idtree == id, trees_list)
    try:
        return list(trees)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)