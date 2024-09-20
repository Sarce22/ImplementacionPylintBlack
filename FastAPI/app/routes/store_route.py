from fastapi import APIRouter, Body, HTTPException
from models.store import Store  # Assuming this is your Pydantic model
from config.database import StoreModel  # Peewee model for the database
from peewee import DoesNotExist

store_route = APIRouter()

# Route to create a new store
@store_route.post("/store")
async def create_store(store: Store = Body(...)):
    try:
        # Create a new store entry in the database
        new_store = StoreModel.create(
            name=store.name,
            address=store.address
        )
        return {"message": "Store created successfully", "store": new_store.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating store: {str(e)}")


# Route to get a store by ID
@store_route.get("/store/{store_id}")
async def get_store(store_id: int):
    try:
        # Fetch the store from the database
        store = StoreModel.get(StoreModel.id == store_id)
        return {"id": store.id, "name": store.name, "address": store.address}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Store not found")


# Route to update a store
@store_route.put("/store/{store_id}")
async def update_store(store_id: int, store: Store = Body(...)):
    try:
        # Update the store in the database
        query = StoreModel.update(
            name=store.name,
            address=store.address
        ).where(StoreModel.id == store_id)
        query.execute()
        return {"message": "Store updated successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Store not found")


# Route to delete a store by ID
@store_route.delete("/store/{store_id}")
async def delete_store(store_id: int):
    try:
        # Delete the store from the database
        store = StoreModel.get(StoreModel.id == store_id)
        store.delete_instance()
        return {"message": "Store deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Store not found")
