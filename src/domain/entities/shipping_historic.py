class ShippingStatus:
    IN_PROGRESS = "Em progresso"
    DONE = "Concluido"
    ERROR = "Erro na formatação do arquivo"


class ShippingHistoric:

    Cpf: str
    Name: str
    Status: str

    def __init__(self, cpf="", name="", status=ShippingStatus.IN_PROGRESS):
        self.Cpf = cpf
        self.Name = name
        self.Status = status

    def serialize(self):
        return {
            "cpf": self.Cpf,
            "name": self.Name,
            "status": self.Status
        }
