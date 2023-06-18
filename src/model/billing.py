import json


class BillingModel:
    def __init__(self, calendar, payer, value, key, payer_request, additional_info):
        self.calendar = calendar
        self.payer = payer
        self.value = value
        self.key = key
        self.payer_request = payer_request
        self.additional_info = additional_info

    def serialize(self):
        data = {
            "calendario": self.calendar,
            "devedor": self.payer,
            "valor": self.value,
            "chave": self.key,
            "solicitacaoPagador": self.payer_request,
            "infoAdicionais": self.additional_info
        }
        return json.dumps(data, indent=2)
