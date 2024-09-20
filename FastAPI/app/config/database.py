import os
from dotenv import load_dotenv
from peewee import *
from datetime import date


# Load environment variables
load_dotenv()

# MySQL database configuration
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

# Store model definition
class StoreModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    address = CharField(max_length=255)

    class Meta:
        database = database
        table_name = "store"  # Table name in the database

# Inventory model definition
class InventoryModel(Model):
    id = AutoField(primary_key=True)
    store_id = ForeignKeyField(StoreModel, backref='inventories', on_delete='CASCADE')
    product_id = IntegerField()
    quantity = IntegerField()

    class Meta:
        database = database
        table_name = "inventory"  # Table name in the database


