from log import logger
from src.services.cnab_processor import CnabProcessor


class ShipmentGenerate:
    def __init__(self):
        pass

    @staticmethod
    def shipment_generate(file):
        process = CnabProcessor(file)
        dados_cnab = process.process()
