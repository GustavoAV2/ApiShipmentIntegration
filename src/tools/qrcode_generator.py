import qrcode
from crcmod import crcmod


class QrCodeGenerator:
    def __init__(self, name, key_pix, value, city, txt_id):
        self.qrcode_string = ""
        self.name = name
        self.key_pix = key_pix
        self.value = value.replace(',', '.')
        self.city = city
        self.txtId = txt_id

        self.name_tam = len(self.name)
        self.key_pix_tam = len(self.key_pix)
        self.value_tam = len(self.value)
        self.city_tam = len(self.city)
        self.txtId_tam = len(self.txtId)
        self.merchantAccount_tam = f'0014BR.GOV.BCB.PIX01{self.key_pix_tam:02}{self.key_pix}'
        self.transactionAmount_tam = f'{self.value_tam:02}{float(self.value):.2f}'
        self.addDataField_tam = f'05{self.txtId_tam:02}{self.txtId}'
        self.name_tam = f'{self.name_tam:02}'
        self.city_tam = f'{self.city_tam:02}'

        self.payloadFormat = '000201'
        self.merchantAccount = f'26{len(self.merchantAccount_tam):02}{self.merchantAccount_tam}'
        self.merchantCategCode = '52040000'
        self.transactionCurrency = '5303986'
        self.transactionAmount = f'54{self.transactionAmount_tam}'
        self.countryCode = '5802BR'
        self.merchantName = f'59{self.name_tam:02}{self.name}'
        self.merchantCity = f'60{self.city_tam:02}{self.city}'
        self.addDataField = f'62{len(self.addDataField_tam):02}{self.addDataField_tam}'
        self.crc16 = '6304'

    def generate_qr_code_string(self):
        self.qrcode_string = f'{self.payloadFormat}{self.merchantAccount}{self.merchantCategCode}' \
                             f'{self.transactionCurrency}{self.transactionAmount}{self.countryCode}' \
                             f'{self.merchantName}{self.merchantCity}{self.addDataField}{self.crc16}'
        return self._generate_crc16(self.qrcode_string)

    def _generate_crc16(self, qrcode_string):
        crc16 = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)

        self.crc16Code = hex(crc16(str(qrcode_string).encode('utf-8')))

        self.crc16Code_formatado = str(self.crc16Code).replace('0x', '').upper().zfill(4)

        self.qrcode_string = f'{qrcode_string}{self.crc16Code_formatado}'

        return self._generate_qr_code(self.qrcode_string)

    def _generate_qr_code(self, qrcode_string):
        self.qrcode = qrcode.make(qrcode_string)
        return qrcode_string

    @staticmethod
    def convert_cnab_json_to_qrcode_json(payload):
        return {
            'name': payload.get('devedor').get('nome') if payload.get('devedor') else "",
            'key': payload.get('chave'),
            'value': payload.get('valor').get('original') if payload.get('valor') else "",
            'txt_id': payload.get('txid')
        }


if __name__ == '__main__':
    payload_data_test = {
        'nome': 'Gustavo Antunes Voltolini',
        'chave': 'gustavoant.voltolini@gmail.com',
        'valor': '100.00',
        'txt_id': 'LOJA01'
    }
    qc = QrCodeGenerator(payload_data_test.get('nome'), payload_data_test.get('chave'),
                         payload_data_test.get('valor'), "", payload_data_test.get('txt_id'))
    st = qc.generate_qr_code_string()
    print(st)
