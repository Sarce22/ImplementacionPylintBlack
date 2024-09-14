from fastapi import APIRouter, Body, HTTPException
from models.store import Store

# Assuming you have a database model similar to `UserModel` for stores.
from database import StoreModel  

store_route = APIRouter()

@store_route.get("/stores")
def get_stores():
    # Logic to fetch and return all stores
    stores = StoreModel.all()
    return stores


@store_route.get("/stores/{store_id}")
def get_store(store_id: str):
    # Logic to fetch and return a specific store by ID
    store = StoreModel.get_or_none(StoreModel.id == store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store


@store_route.post("/stores")
def create_store(store: Store = Body(...)):
    # Logic to create a new store
    new_store = StoreModel.create(
        id=store.id, nombre=store.nombre, direccion=store.direccion
    )
    return new_store


@store_route.put("/stores/{store_id}")
def update_store(store_id: str, store_data: Store = Body(...)):
    # Logic to update a store by ID
    store = StoreModel.get_or_none(StoreModel.id == store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    store.nombre = store_data.nombre
    store.direccion = store_data.direccion
    store.save()
    return store


@store_route.delete("/stores/{store_id}")
def delete_store(store_id: str):
    # Logic to delete a store by ID
    store = StoreModel.get_or_none(StoreModel.id == store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    store.delete_instance()
    return {"message": "Store deleted successfully"}