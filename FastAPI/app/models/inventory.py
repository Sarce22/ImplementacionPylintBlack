from pydantic import BaseModel

class Inventory(BaseModel):
    """
    Represents an inventory item.

    Attributes:
        id (int): The unique identifier of the inventory item.
        shop_id (int): The identifier of the shop that owns the inventory item.
        product_id (int): The identifier of the product that the inventory item represents.
        quantity (int): The quantity of the product in the inventory.
    """
    id: int
    shop_id: int
    product_id: int
    quantity: int