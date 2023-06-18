from src.log import logger
from src.database.mongo_connection import MongoDbConnection
from src.domain.entities.shipping_historic import ShippingHistoric, ShippingStatus


class DatabaseActions:
    def __init__(self):
        self.db = MongoDbConnection()

    def insert_error_shipment(self, data, status=ShippingStatus.ERROR_FORMAT):
        cpf = data.get('devedor').get('cpf') if data.get('devedor') else ""
        name = data.get('devedor').get('nome') if data.get('devedor') else ""
        qr_code_string = data.get('qr_code_string')
        shipment_historic = ShippingHistoric(cpf=cpf, name=name, qr_code_string=qr_code_string, status=status)
        self.db.insert_shipment(shipment_historic.serialize())

    def insert_done_shipment(self, data):
        shipment_historic = ShippingHistoric(data['devedor']['cpf'], data['devedor']['nome'],
                                             qr_code_string=data["qr_code_string"], status=ShippingStatus.DONE)
        self.db.insert_shipment(shipment_historic.serialize())

    def get_all_historic(self):
        try:
            historic_shipments = self.db.get_historic_shipments()
            return [ShippingHistoric(cpf=historic.get('cpf'), name=historic.get('name'),
                                     qr_code_string=historic.get('qr_code_string'),
                                     created_date=historic.get('created_date'),
                                     status=historic.get('status')) for historic in historic_shipments]
        except Exception as ex:
            logger.info(f"Erro ao buscar historico: {ex.args}")
            return []

    def get_historic_by_filename(self, filename):
        historic = self.db.find_by_params({"filename": filename})
        return historic
