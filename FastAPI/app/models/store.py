"""
This module defines the Store model using Pydantic.
"""

from pydantic import BaseModel


class Store(BaseModel):
    """
    A Pydantic model representing a store.

    Attributes:
        id (str): The unique identifier of the store.
        nombre (str): The name of the store.
        direccion (str): The address of the store.
    """
    id: str
    name: str
    address: str