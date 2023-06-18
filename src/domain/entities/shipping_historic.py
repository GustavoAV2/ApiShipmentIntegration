from datetime import datetime


class ShippingStatus:
    IN_PROGRESS = "Em progresso"
    DONE = "Concluido"
    ERROR_FORMAT = "Erro na formatação do arquivo"
    ERROR_REQUEST = "Erro na requisição para na API-PIX"


class ShippingHistoric:

    Cpf: str
    Name: str
    Status: str
    CreatedDate = None
    QrCodeString: str

    def __init__(self, cpf="", name="", created_date=None, qr_code_string="", status=ShippingStatus.IN_PROGRESS):
        self.Cpf = cpf
        self.Name = name
        self.Status = status
        self.QrCodeString = qr_code_string
        self.CreatedDate = created_date if created_date else datetime.now()

    def serialize(self):
        return {
            "cpf": self.Cpf,
            "name": self.Name,
            "status": self.Status,
            "qr_code_string": self.QrCodeString,
            "created_date": self.CreatedDate.strftime("%d/%m/%Y %H:%M:%S")
        }
