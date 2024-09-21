"""
This module contains the API routes for managing inventory in the FastAPI application.
"""

from fastapi import APIRouter, Body, HTTPException
from models.inventory import Inventory
from config.database import InventoryModel

inventory_route = APIRouter()


@inventory_route.post("/inventory")
def create_inventory(inventory: Inventory = Body(...)):
    """
    Create a new inventory item.
    """
    new_inventory = InventoryModel.create(
        id=inventory.id,
        shop_id=inventory.shop_id,
        product_id=inventory.product_id,
        quantity=inventory.quantity,
    )
    return new_inventory


@inventory_route.get("/inventory")
def get_inventory():
    """
    Fetch and return all inventory items.
    """
    inventory = InventoryModel.all()
    return inventory


@inventory_route.get("/inventory/{inventory_id}")
def get_inventory_by_id(inventory_id: str):
    """
    Fetch and return a specific inventory item by ID.
    """
    inventory = InventoryModel.get_or_none(InventoryModel.id == inventory_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory


@inventory_route.put("/inventory/{inventory_id}")
def update_inventory(inventory_id: str, inventory_data: Inventory = Body(...)):
    """
    Update an inventory item by ID.
    """
    inventory = InventoryModel.get_or_none(InventoryModel.id == inventory_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    inventory.shop_id = inventory_data.shop_id
    inventory.product_id = inventory_data.product_id
    inventory.quantity = inventory_data.quantity
    inventory.save()
    return inventory


@inventory_route.delete("/inventory/{inventory_id}")
def delete_inventory(inventory_id: str):
    """
    Delete an inventory item by ID.
    """
    inventory = InventoryModel.get_or_none(InventoryModel.id == inventory_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    inventory.delete_instance()
    return {"message": "Inventory deleted successfully"}
