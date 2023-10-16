from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel

#Objetos
class ProgrammingL(BaseModel):
    id: int
    name: str
    openSource: bool

programings_list = [
    ProgrammingL(id=1, name="Python", openSource=True),
    ProgrammingL(id=2, name="C++", openSource=False),
    ProgrammingL(id=3, name="C#", openSource=False),
    ProgrammingL(id=4, name="C", openSource=False),
    ProgrammingL(id=5, name="Java", openSource=True),
]

#Router
routerProgramins = APIRouter()

@routerProgramins.get("/9/", status_code=status.HTTP_200_OK)
async def programingsclass():
    return programings_list

@routerProgramins.get("/9/{id}", status_code=status.HTTP_200_OK)
async def programingsclass(id: int):
    programings = filter(lambda program: program.id == id, programings_list)
    try:
        return list(programings)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)