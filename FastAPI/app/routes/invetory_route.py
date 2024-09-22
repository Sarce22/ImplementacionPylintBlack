"""
This module contains the API routes for managing inventory in the FastAPI application.
"""

from fastapi import APIRouter, Body, HTTPException
from models.inventory import Inventory
from services.inventory_service import InventoryService

inventory_route = APIRouter()

@inventory_route.post("/inventory")
def create_inventory(inventory: Inventory = Body(...)):
    """Create a new inventory item."""
    try:
        new_inventory = InventoryService.create_inventory(
            shop_id=inventory.shop_id,
            product_id=inventory.product_id,
            quantity=inventory.quantity
        )
        return {
            "message": "Inventory item created",
            "inventory": new_inventory
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while creating the inventory"
        ) from exc


@inventory_route.get("/inventory")
def get_inventory():
    """Fetch and return all inventory items."""
    try:
        inventory = InventoryService.get_all_inventory()
        return inventory
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while fetching the inventory"
        ) from exc


@inventory_route.get("/inventory/{inventory_id}")
def get_inventory_by_id(inventory_id: str):
    """Fetch and return a specific inventory item by ID."""
    try:
        inventory = InventoryService.get_inventory_by_id(inventory_id)
        if not inventory:
            raise HTTPException(status_code=404, detail="Inventory not found")
        return inventory
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while fetching the inventory item"
        ) from exc


@inventory_route.put("/inventory/{inventory_id}")
def update_inventory(inventory_id: str, inventory_data: Inventory = Body(...)):
    """Update an inventory item by ID."""
    try:
        updated_inventory = InventoryService.update_inventory(inventory_id, inventory_data)
        if not updated_inventory:
            raise HTTPException(status_code=404, detail="Inventory not found")
        return {
            "message": "Inventory updated",
            "inventory": updated_inventory
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while updating the inventory"
        ) from exc


@inventory_route.delete("/inventory/{inventory_id}")
def delete_inventory(inventory_id: str):
    """Delete an inventory item by ID."""
    try:
        success = InventoryService.delete_inventory(inventory_id)
        if not success:
            raise HTTPException(status_code=404, detail="Inventory not found")
        return {"message": "Inventory deleted successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while deleting the inventory"
        ) from exc
