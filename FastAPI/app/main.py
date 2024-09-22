"""
Main module for the FastAPI application.

This module initializes the FastAPI app and sets up the database connection
management and route inclusion.
"""

from contextlib import asynccontextmanager  
from fastapi import FastAPI, Depends
from helpers.api_key_auth import get_api_key
from starlette.responses import RedirectResponse

# Base de datos
from config.database import database as connection
from routes.store_route import store_route
from routes.invetory_route import inventory_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager to manage the lifespan of the FastAPI application.

    Connects to the database when the application starts and closes the connection
    when the application stops.

    Args:
        application (FastAPI): The FastAPI application instance.
    """
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        if not connection.is_closed():
            connection.close()


app = FastAPI(
    title="Pylint Implementacion",
    version="2.0",
    contact={"name": "Juan Pablo Acosta Y Sebastian Arce", 
             "url": "https://github.com/Sarce22/ImplementacionPylintBlack",
             "email": "sebastian@gmail.com"},
)


@app.get("/")
async def read_root() -> RedirectResponse:
    """
    Redirects the root URL to the FastAPI documentation.

    Returns:
        RedirectResponse: A redirect response to the FastAPI documentation page.
    """
    return RedirectResponse(url="/docs")


# Include routers for store and inventory routes
app.include_router(store_route, prefix="/api/tienda", tags=["Store"], dependencies=[Depends(get_api_key)])
app.include_router(inventory_route, prefix="/api/inventario", tags=["Inventory"], dependencies=[Depends(get_api_key)])
