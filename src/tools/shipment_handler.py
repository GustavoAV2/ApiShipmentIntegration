from typing import Dict
from datetime import datetime
from src.log import logger
from src.domain.models.calendar import Calendar
from src.tools.cnab_handler import CnabHandler


class ShipmentHandler:
    def __init__(self):
        self.cnab_handler = CnabHandler()

    def shipment_generate(self, file) -> Dict:
        try:
            cnab_data = self.cnab_handler.convert_to_dict(file)
            shipment = self._assemble_shipment(cnab_data)
            return shipment
        except Exception as ex:
            logger.info(f"Erro: {ex.args}")
            return {}

    def shipment_generate_bytes(self, file) -> Dict:
        try:
            cnab_data = self.cnab_handler.convert_to_dict(file)
            shipment = self._assemble_shipment(cnab_data)
            return shipment
        except Exception as ex:
            logger.info(f"Erro: {ex.args}")
            return {}

    @staticmethod
    def _assemble_shipment(cnab_data) -> Dict:
        detail_info = cnab_data['detail_data']
        additional_info = cnab_data['additional_data']
        shipment = {}
        expiration_timestamp = datetime(int(detail_info['expiration_timestamp'][0:4])
                                        , int(detail_info['expiration_timestamp'][4:6])
                                        , int(detail_info['expiration_timestamp'][6:8])
                                        , int(detail_info['expiration_timestamp'][8:10])
                                        , int(detail_info['expiration_timestamp'][10:12])
                                        , int(detail_info['expiration_timestamp'][12:14]))
        expiration_seconds = (expiration_timestamp - datetime.now()).seconds
        shipment['calendario'] = Calendar(expiration_seconds).serialize()
        debtor_info = {
            'debtor_type': 'cpf' if detail_info['debtor_person_type'] == '01' else 'cnpj',
            'debtor_id': detail_info['debtor_cpf_cnpj'],
            'debtor_name': detail_info['debtor_name']
        }
        shipment['devedor'] = {}
        if debtor_info['debtor_type'] == 'cpf':
            shipment['devedor']['cpf'] = debtor_info['debtor_id']
        else:
            shipment['devedor']['cnpj'] = debtor_info['debtor_id']
        shipment['devedor']['nome'] = debtor_info['debtor_name']

        original_value = detail_info['original_value'][0:15] + '.' + detail_info['original_value'][15:]
        value_info = {
            'original': original_value,
            'modalidadeAlteracao': 0 if detail_info['billing_type'] == '1' and original_value == '' else 1
        }
        shipment['valor'] = value_info
        shipment['chave'] = detail_info['pix_key']
        shipment['solicitacaoPagador'] = detail_info['payer_request']
        shipment['infoAdicionais'] = [
            {'nome': additional_info['name_one'], 'valor': additional_info['value_one']},
            {'nome': additional_info['name_two'], 'valor': additional_info['value_two']}
        ]

        return shipment

    def generate_cnab750_file(self, data):
        return
