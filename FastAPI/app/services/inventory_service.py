"""
Module that provides service functionality for managing inventory in the database.
"""

from peewee import DoesNotExist
from config.database import InventoryModel


class InventoryService:
    """Service class for handling business logic related to inventory."""

    @staticmethod
    def create_inventory(
        shop_id: int, product_id: int, quantity: int
    ) -> InventoryModel:
        """Creates a new inventory item in the database."""
        try:
            return InventoryModel.create(
                shop_id=shop_id, product_id=product_id, quantity=quantity
            )
        except Exception as exc:
            raise RuntimeError(f"Error creating inventory item: {exc}") from exc

    @staticmethod
    def get_all_inventory() -> list:
        """Retrieves all inventory items from the database."""
        try:
            return list(InventoryModel.select())
        except Exception as exc:
            raise RuntimeError(f"Error fetching inventory: {exc}") from exc

    @staticmethod
    def get_inventory_by_id(inventory_id: str) -> InventoryModel:
        """Retrieves an inventory item by ID."""
        try:
            return InventoryModel.get_or_none(InventoryModel.id == inventory_id)
        except Exception as exc:
            raise RuntimeError(f"Error fetching inventory item: {exc}") from exc

    @staticmethod
    def update_inventory(inventory_id: str, inventory_data) -> InventoryModel:
        """Updates an inventory item in the database."""
        try:
            inventory = InventoryModel.get_or_none(InventoryModel.id == inventory_id)
            if not inventory:
                return None
            inventory.shop_id = inventory_data.shop_id
            inventory.product_id = inventory_data.product_id
            inventory.quantity = inventory_data.quantity
            inventory.save()
            return inventory
        except DoesNotExist:
            return None
        except Exception as exc:
            raise RuntimeError(f"Error updating inventory item: {exc}") from exc

    @staticmethod
    def delete_inventory(inventory_id: str) -> bool:
        """Deletes an inventory item from the database."""
        try:
            inventory = InventoryModel.get_or_none(InventoryModel.id == inventory_id)
            if not inventory:
                return False
            inventory.delete_instance()
            return True
        except Exception as exc:
            raise RuntimeError(f"Error deleting inventory item: {exc}") from exc
