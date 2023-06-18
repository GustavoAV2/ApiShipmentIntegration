from src.domain.model.billing import BillingModel


class BillingFactory:
    @staticmethod
    def generate_billing(json_data):
        return BillingModel()
