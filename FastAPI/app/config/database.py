from dotenv import load_dotenv
from peewee import *
from datetime import date

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class TiendaModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"


class InventarioModel(Model):
    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref='orders', on_delete='CASCADE')
    item_id = IntegerField()
    total_amount = FloatField()
    status = CharField(max_length=50)
    date = DateField(default=date.today)

    class Meta:
        database = database
        table_name = "orders"