from pydantic import BaseModel


class Store(BaseModel):
    """
    Represents an Store item.

    Attributes:
        id (int): The unique identifier of the store item.
        name (store): The identifier of the shop that owns the inventory item.
        address (str): The identifier of the product that the inventory item represents.
    """
    id: int
    name: str
    address: str