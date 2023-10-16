from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

class Student (BaseModel):
    idstudent: int
    name: str
    edad: int

students_list = [
    Student(idstudent=1, name="Areli", edad=30),
    Student(idstudent=2, name="Balcón", edad=45),
    Student(idstudent=3, name="Pérez", edad=22),
    Student(idstudent=4, name="Jonathan", edad=23),
    Student(idstudent=5, name="Abdiel", edad=20)
]

routerStudents = APIRouter()

@routerStudents.get("/4/", status_code=status.HTTP_200_OK)
async def studentsclass():
    return students_list

@routerStudents.get("/4/{id}", status_code=status.HTTP_200_OK)
async def studentsclass(id: int):
    students = filter(lambda student: student.idstudent == id, students_list)
    try:
        return list(students)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)