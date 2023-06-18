from src.log import logger
from src.database.mongo_connection import MongoDbConnection
from src.domain.entities.shipping_historic import ShippingHistoric, ShippingStatus


class DatabaseActions:
    def __init__(self):
        self.db = MongoDbConnection()

    def insert_error_shipment(self, data):
        cpf = data.get('devedor').get('cpf') if data.get('devedor') else ""
        name = data.get('devedor').get('nome') if data.get('devedor') else ""
        shipment_historic = ShippingHistoric(cpf, name, ShippingStatus.ERROR)
        self.db.insert_shipment(shipment_historic.serialize())

    def insert_done_shipment(self, data):
        shipment_historic = ShippingHistoric(data['devedor']['cpf'], data['devedor']['nome'], ShippingStatus.DONE)
        self.db.insert_shipment(shipment_historic.serialize())

    def get_all_historic(self):
        try:
            historic_shipments = self.db.get_historic_shipments()
            return [ShippingHistoric(historic.get('cpf'), historic.get('name'), historic.get('created_date'), historic.get('status')) for historic in historic_shipments]
        except Exception as ex:
            logger.info(f"Erro ao buscar historico: {ex.args}")
            return []
