from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Standard imports should come first
from contextlib import asynccontextmanager

# Database connection
from app.config.database import database as connection  # Adjusted import path

# Routes
from ..app.routes.inventory_route import inventory_route  # Adjusted import path


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage the lifespan of the application, ensuring the database connection is handled properly."""
    # Connect to the database if it's closed
    if connection.is_closed():
        connection.connect()
    try:
        yield  # This is where the application will run
    finally:
        # Close the connection when the app stops
        if not connection.is_closed():
            connection.close()


# Initialize FastAPI app
app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    """Redirect to the API docs."""
    return RedirectResponse(url="/docs")


# Include inventory routes
app.include_router(inventory_route, prefix="/api/tienda", tags=["tienda"])
