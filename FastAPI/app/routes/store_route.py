"""
This module contains the API routes for managing stores in the FastAPI application.
"""

from fastapi import APIRouter, Body, HTTPException
from ..models.store import Store  # Importing the Store model correctly
from ..config.database import StoreModel  # Assuming you have a database model for stores.

store_route = APIRouter()


@store_route.get("/stores")
def get_stores():
    """
    Fetch and return all stores.
    """
    stores = StoreModel.all()
    return stores


@store_route.get("/stores/{store_id}")
def get_store(store_id: str):
    """
    Fetch and return a specific store by ID.
    """
    store = StoreModel.get_or_none(StoreModel.id == store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store


@store_route.post("/stores")
def create_store(store: Store = Body(...)):
    """
    Create a new store with the provided details.
    """
    new_store = StoreModel.create(
        id=store.id, nombre=store.name, direccion=store.address
    )
    return new_store


@store_route.put("/stores/{store_id}")
def update_store(store_id: str, store_data: Store = Body(...)):
    """
    Update an existing store by ID with new details.
    """
    store = StoreModel.get_or_none(StoreModel.id == store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    store.nombre = store_data.name
    store.direccion = store_data.address
    store.save()
    return store


@store_route.delete("/stores/{store_id}")
def delete_store(store_id: str):
    """
    Delete a store by ID.
    """
    store = StoreModel.get_or_none(StoreModel.id == store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    store.delete_instance()
    return {"message": "Store deleted successfully"}