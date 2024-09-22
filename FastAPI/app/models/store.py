"""
Module for defining the Store model.

This module contains the Pydantic model representing a store,
including its attributes and validations.
"""

from pydantic import BaseModel


class Store(BaseModel):
    """
    Represents a store item.

    Attributes:
        id (int): The unique identifier of the store.
        name (str): The name of the store.
        address (str): The address of the store.
    """
    id: int
    name: str
    address: str
