from log import logger
from src.tools.shipment_handler import ShipmentHandler
from src.tools.file_handler import FileManager
from src.actions.database_actions import DatabaseActions


class ShipmentActions:
    def __init__(self):
        self.shipment_handler = ShipmentHandler()
        self.file_manager = FileManager()
        self.db = DatabaseActions()

    def send_converted_file(self, file_path):
        filename = self.file_manager.get_filename(file_path)
        shipment_dict = self.shipment_handler.shipment_generate(filename)
        if not shipment_dict:
            logger.info("Erro ao tratar arquivo, registrando no banco de dados e encerrando operação!")
            self.db.insert_error_shipment(shipment_dict)
            return
        logger.info("Arquivo tratado com sucesso!")
        logger.info("Enviando solicitação de cobrança a API-PIX!")
        logger.info("Gerando QR CODE!")
        # self.file_manager.write_file() # Inserir no banco
        self.db.insert_done_shipment(shipment_dict)
        logger.info("Status da remessa registrada")
