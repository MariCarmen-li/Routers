from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

class Auto (BaseModel):
    autoid: int
    nombre: str
    marca: str
    modelo: int

#Creamos una lista de autos para mostrar
auto_list = [
    Auto(autoid=1, nombre="Bocho", marca="Volkswagen", modelo = 1990),
    Auto(autoid=2, nombre="Atitute", marca="Doch", modelo=2008),
    Auto(autoid=3, nombre="Vento", marca="Volkswagen", modelo=2020),
    Auto(autoid=4, nombre="Jetta", marca="Volkswagen", modelo=2023),
    Auto(autoid=5, nombre="Tsuru", marca="Nissan", modelo=1999)
]

#Levantamos el router de este archivo
routerAutos = APIRouter()

@routerAutos.get("/1/", status_code=status.HTTP_200_OK)
async def returnAutos():
    return auto_list

@routerAutos.get("/1/{id}", status_code=status.HTTP_200_OK)
async def returnAutos(id: int):
    autos = filter(lambda auto: auto.autoid == id, auto_list)
    try:
        return list(autos)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
