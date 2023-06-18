from pixqrcodegen import Payload


class PayloadQRCodeGenerator:
    def __init__(self, payload_data):
        self.payload_data = payload_data

    def gerar_qr_code(self):
        payload = Payload(self.payload_data['nome'], self.payload_data['chave'], self.payload_data['valor'],
                          self.payload_data['cidade'], self.payload_data['txt_id'])
        payload.gerarPayload()


if __name__ == '__main__':
    payload_data_test = {
        'nome': 'Gustavo Antunes Voltolini',
        'chave': 'gustavoant.voltolini@gmail.com',
        'valor': '100.00',
        'cidade': 'SAO PAULO',
        'txt_id': 'LOJA01'
    }
    generator = PayloadQRCodeGenerator(payload_data_test)
    generator.gerar_qr_code()
