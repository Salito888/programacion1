
from fastapi import FastAPI
from api.controller.cuenta_controller import router as cuenta_router
app = FastAPI()

# Se deben incluir las rutas del controlador de cuentas
app.include_router(cuenta_router, prefix="/api/cuentas")
@app.get("/")
def leer_raiz():
    return {"mensaje": "Bienvenido a la API de gestión de cuentas bancarias"}
