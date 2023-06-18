from src.model.billing import BillingModel
from src.model.sub_models import *


class BillingFactory:
    @staticmethod
    def generate_billing(json_data):
        return BillingModel()
