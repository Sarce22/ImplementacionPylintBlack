from fastapi import APIRouter, Body, HTTPException
from models.inventory import inventory  # Assuming this is your Pydantic model
from config.database import InventoryModel  # Peewee model for the database
from peewee import DoesNotExist

inventory_route = APIRouter()

# Route to create a new inventory record
@inventory_route.post("/inventory")
async def create_inventory(inventory: inventory = Body(...)):
    try:
        # Create a new inventory entry in the database
        new_inventory = InventoryModel.create(
            tienda_id=inventory.tienda_id,
            producto_id=inventory.producto_id,
            cantidad=inventory.cantidad
        )
        return {"message": "Inventory created successfully", "inventory_id": new_inventory.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating inventory: {str(e)}")


# Route to get inventory by ID
@inventory_route.get("/inventory/{inventory_id}")
async def get_inventory(inventory_id: int):
    try:
        # Fetch the inventory record from the database
        inventory = inventaryModel.get(inventaryModel.id == inventory_id)
        return {
            "id": inventory.id,
            "tienda_id": inventory.tienda_id.id,
            "producto_id": inventory.producto_id,
            "cantidad": inventory.cantidad
        }
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Inventory not found")


# Route to update an inventory record
@inventory_route.put("/inventory/{inventory_id}")
async def update_inventory(inventory_id: int, inventory: Inventory = Body(...)):
    try:
        # Update the inventory record in the database
        query = inventaryModel.update(
            tienda_id=inventory.tienda_id,
            producto_id=inventory.producto_id,
            cantidad=inventory.cantidad
        ).where(inventaryModel.id == inventory_id)
        query.execute()
        return {"message": "Inventory updated successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Inventory not found")


# Route to delete an inventory record
@inventory_route.delete("/inventory/{inventory_id}")
async def delete_inventory(inventory_id: int):
    try:
        # Delete the inventory record from the database
        inventory = inventaryModel.get(inventaryModel.id == inventory_id)
        inventory.delete_instance()
        return {"message": "Inventory deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Inventory not found")
