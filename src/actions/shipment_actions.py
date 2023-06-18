from src.domain.entities.shipping_historic import ShippingStatus
from src.log import logger
from src.actions.client.pix_client import PixClient
from src.tools.shipment_handler import ShipmentHandler
from src.tools.file_handler import FileManager
from src.tools.qrcode_generator import QrCodeGenerator
from src.actions.database_actions import DatabaseActions


class ShipmentActions:
    def __init__(self):
        self.pix_client = PixClient()
        self.shipment_handler = ShipmentHandler()
        self.file_manager = FileManager()
        self.db = DatabaseActions()
        self.qr_code = None

    def send_converted_file(self, file, file_id):
        filename = self.create_name(file_id)
        self.file_manager.write_file(filename, file.file, self.file_manager.INPUT_PATH)
        shipment_dict = self.shipment_handler.shipment_generate(filename)
        if not shipment_dict:
            logger.info("Erro ao tratar arquivo, registrando no banco de dados status de erro na formatação!")
            self.db.insert_error_shipment(shipment_dict)
            return False

        logger.info("Arquivo tratado com sucesso!")
        logger.info("Enviando solicitação de COBRANÇA a API-PIX!")
        response = self.pix_client.request_create_cob(shipment_dict)
        if not self.pix_client.valid_response(response):
            logger.info(f"Erro ao criar cobrança na API-PIX, registrando no banco de dados e encerrando operação!")
            self.db.insert_error_shipment(shipment_dict, ShippingStatus.ERROR_REQUEST)

        logger.info("Solicitação de COBRANÇA realizada com sucesso!")
        logger.info("Gerando QR CODE!")
        shipment_dict['qr_code_string'] = self.create_payment_qr_code(response.get('data'))
        shipment_dict['filename'] = filename
        self.file_manager.write_file(filename, file.file, self.file_manager.SEND_PATH)
        self.db.insert_done_shipment(shipment_dict)
        logger.info("Status da remessa registrada como Concluido")
        return True

    def download_file_data_shipment(self, file_id):
        filename = self.create_name(file_id)
        file = self.file_manager.get_file(filename, self.file_manager.SEND_PATH)
        historic = self.db.get_historic_by_filename(filename)
        return {
            "file": file,
            "historic": historic if historic else None
        }

    def create_payment_qr_code(self, payload):
        try:
            self.qr_code = QrCodeGenerator(payload.get('devedor').get("nome"),
                                           payload.get('chave'),
                                           payload.get('valor').get("original"), "",
                                           payload.get('txid'))
            return self.qr_code.generate_qr_code_string()
        except Exception as ex:
            logger.info(f"Não foi possível criar o QRCode, erro: {ex.args}")

    @staticmethod
    def create_name(file_id):
        filename = file_id + ".txt"
        filename = filename.replace("'", "")
        filename.strip()
        return filename
