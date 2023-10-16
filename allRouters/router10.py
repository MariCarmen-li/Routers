from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel

#Objects
class Subject(BaseModel):
    idsubject: int
    name: str
    numberStudents: int

subjects_list= [
    Subject(idsubject=1, name="Math", numberStudents=23),
    Subject(idsubject=2, name="English", numberStudents=34),
    Subject(idsubject=3, name="Biology", numberStudents=40),
    Subject(idsubject=4, name="Physics", numberStudents=37),
    Subject(idsubject=5, name="Chemistry", numberStudents=20)
]

#Router with fastapi
routerSubject = APIRouter()

@routerSubject.get("/10/", status_code=status.HTTP_200_OK)
async def subjectsclass():
    return subjects_list

@routerSubject.get("/10/{id}", status_code=status.HTTP_200_OK)
async def subjectclass(id: int):
    subjects = filter(lambda sub: sub.idsubject == id, subjects_list)
    try:
        return list(subjects)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)