from src.actions.client.pix_client import PixClient
from src.database.mongo_connection import MongoDbConnection


class ShipmentActions:
    def __init__(self):
        self.db = MongoDbConnection()
        self.client = PixClient()



