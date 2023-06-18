from src.domain.model.sub_models.additional_info import AdditionalInfo
from src.domain.model.sub_models.calendar import Calendar
from src.domain.model.sub_models.debtor import Debtor


class Shipment:
    def __init__(self, calendar: Calendar, debtor: Debtor, loc,
                 value, key, payer_request, additional_info: AdditionalInfo):
        self.calendar = calendar
        self.debtor = debtor
        self.loc = loc
        self.value = value
        self.key = key
        self.payer_request = payer_request
        self.additional_info = additional_info
