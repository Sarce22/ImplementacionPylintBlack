"""
This module contains the API routes for managing stores in the FastAPI application.
"""

from fastapi import APIRouter, Body, HTTPException
from models.store import Store
from services.store_service import StoreService

store_route = APIRouter()

@store_route.get("/stores")
def get_stores():
    """Fetch and return all stores."""
    try:
        stores = StoreService.get_all_stores()
        return stores
    except Exception as exc:
        raise HTTPException(status_code=500, detail="An error occurred while fetching stores") from exc


@store_route.get("/stores/{store_id}")
def get_store(store_id: str):
    """Fetch and return a specific store by ID."""
    try:
        store = StoreService.get_store_by_id(store_id)
        if not store:
            raise HTTPException(status_code=404, detail="Store not found")
        return store
    except Exception as exc:
        raise HTTPException(status_code=500, detail="An error occurred while fetching the store") from exc


@store_route.post("/stores")
def create_store(store: Store = Body(...)):
    """Create a new store with the provided details."""
    try:
        new_store = StoreService.create_store(
            id=store.id, name=store.name, address=store.address
        )
        return {"message": "Store created", "store": new_store}
    except Exception as exc:
        raise HTTPException(status_code=500, detail="An error occurred while creating the store") from exc


@store_route.put("/stores/{store_id}")
def update_store(store_id: str, store_data: Store = Body(...)):
    """Update an existing store by ID with new details."""
    try:
        updated_store = StoreService.update_store(store_id, store_data)
        if not updated_store:
            raise HTTPException(status_code=404, detail="Store not found")
        return {"message": "Store updated", "store": updated_store}
    except Exception as exc:
        raise HTTPException(status_code=500, detail="An error occurred while updating the store") from exc


@store_route.delete("/stores/{store_id}")
def delete_store(store_id: str):
    """Delete a store by ID."""
    try:
        success = StoreService.delete_store(store_id)
        if not success:
            raise HTTPException(status_code=404, detail="Store not found")
        return {"message": "Store deleted successfully"}
    except Exception as exc:
        raise HTTPException(status_code=500, detail="An error occurred while deleting the store") from exc
