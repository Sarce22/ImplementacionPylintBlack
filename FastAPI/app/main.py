from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Base de datos
from FastAPI.app.database import database as connection

from routes.tienda_route import tienda_route
from routes.tienda_route import tienda_route



from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


app.include_router(tienda_route, prefix="/api/tienda", tags=["tienda"])
