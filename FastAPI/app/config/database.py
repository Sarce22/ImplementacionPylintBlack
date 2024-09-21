"""Database models for the FastAPI application.

This module contains the database models used for the application,
including StoreModel and InventoryModel.
"""

from datetime import date
import os
from dotenv import load_dotenv
from peewee import *

load_dotenv()

# Database configuration
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class StoreModel(Model):
    """Model representing a store user.

    Attributes:
        id (AutoField): Primary key for the user.
        username (CharField): Username of the user.
        email (CharField): Email address of the user.
        password (CharField): Password for the user's account.
    """

    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"


class InventoryModel(Model):
    """Model representing an inventory item associated with a user.

    Attributes:
        id (AutoField): Primary key for the inventory item.
        user_id (ForeignKeyField): Foreign key referencing a user in the StoreModel.
        item_id (IntegerField): Identifier for the inventory item.
        total_amount (FloatField): Total amount of the item.
        status (CharField): Status of the inventory item.
        date (DateField): Date when the inventory record was created.
    """

    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(StoreModel, backref="orders", on_delete="CASCADE")
    item_id = IntegerField()
    total_amount = FloatField()
    status = CharField(max_length=50)
    date = DateField(default=date.today)

    class Meta:
        database = database
        table_name = "orders"
