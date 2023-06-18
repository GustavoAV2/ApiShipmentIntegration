
class ShippingStatus:
    PENDING = "1"
    DONE = "2"
    ERROR = "3"


class Shipping:
    def __init__(self, tax_id="", status=ShippingStatus.PENDING):
        self.TaxId = tax_id
        self.Status = status

    Id: str
    Status: str
    TaxId: str
