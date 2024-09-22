"""
Module that provides service functionality for managing stores in the database.
"""

from peewee import DoesNotExist
from config.database import StoreModel


class StoreService:
    """Service class for handling business logic related to stores."""

    @staticmethod
    def create_store(id_store: int, name: str, address: str) -> StoreModel:
        """Creates a new store in the database."""
        try:
            return StoreModel.create(id=id_store, nombre=name, direccion=address)
        except Exception as exc:
            raise RuntimeError(f"Error creating store: {exc}") from exc

    @staticmethod
    def get_all_stores() -> list:
        """Retrieves all stores from the database."""
        try:
            return list(StoreModel.select())
        except Exception as exc:
            raise RuntimeError(f"Error fetching stores: {exc}") from exc

    @staticmethod
    def get_store_by_id(store_id: str) -> StoreModel:
        """Retrieves a store by ID."""
        try:
            return StoreModel.get_or_none(StoreModel.id == store_id)
        except Exception as exc:
            raise RuntimeError(f"Error fetching store: {exc}") from exc

    @staticmethod
    def update_store(store_id: str, store_data) -> StoreModel:
        """Updates a store in the database."""
        try:
            store = StoreModel.get_or_none(StoreModel.id == store_id)
            if not store:
                return None
            store.nombre = store_data.name
            store.direccion = store_data.address
            store.save()
            return store
        except DoesNotExist:
            return None
        except Exception as exc:
            raise RuntimeError(f"Error updating store: {exc}") from exc

    @staticmethod
    def delete_store(store_id: str) -> bool:
        """Deletes a store from the database."""
        try:
            store = StoreModel.get_or_none(StoreModel.id == store_id)
            if not store:
                return False
            store.delete_instance()
            return True
        except Exception as exc:
            raise RuntimeError(f"Error deleting store: {exc}") from exc
