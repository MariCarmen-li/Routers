#Importamos nuestro framwork
from fastapi import FastAPI
#Importamos nuestros 10 routers
from allRouters import router1, router2, router3, router4, router5, router6, router7, router8, router9, router10

#Levantamos nuestra instancia de fastAPI
app = FastAPI()

#Incluimos los 10 routers
app.include_router(router1.routerAutos)
app.include_router(router2.routerUsuario)
app.include_router(router3.routerAnimals)
app.include_router(router4.routerStudents)
app.include_router(router5.routerTrees)
app.include_router(router6.routerShoes)
app.include_router(router7.routerComputers)
app.include_router(router8.routerLobo)
app.include_router(router9.routerProgramins)
app.include_router(router10.routerSubject)


#Hcaemos un path del main (opcional)
@app.get("/")
async def imprimir():
    return "Hola mundo"