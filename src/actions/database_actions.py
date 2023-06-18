from src.database.mongo_connection import MongoDbConnection
from src.domain.entities.shipping_historic import ShippingHistoric, ShippingStatus


class DatabaseActions:
    def __init__(self):
        self.db = MongoDbConnection()

    def insert_error_shipment(self, data):
        shipment_historic = ShippingHistoric(data['devedor']['cpf'], data['devedor']['nome'], ShippingStatus.ERROR)
        self.db.insert_shipment(shipment_historic.serialize())

    def insert_done_shipment(self, data):
        shipment_historic = ShippingHistoric(data['devedor']['cpf'], data['devedor']['nome'], ShippingStatus.DONE)
        self.db.insert_shipment(shipment_historic.serialize())
