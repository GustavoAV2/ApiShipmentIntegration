import requests
from src.domain.entities.shipping import Shipping
from src.domain.model.billing import BillingModel


class PixClient:
    def __init__(self):
        self.url = "https://pix.example.com/"
        self.token = ""
        self.client_id = "citiClientTest"
        self.client_secret = "citiClientTest"

    def _request_authorize_token(self):
        if self.token:
            return self.token
        try:
            payload = {"client_id": self.client_id, "client_secret": self.client_secret}
            response = requests.post(self.url + 'oauth/token', data=payload)
            return response.json()
        except Exception as ex:
            return {}

    def request_create_billing(self, billing_model: BillingModel):
        self.token = self._request_authorize_token()
        try:
            response = requests.post(self.url + 'cob',
                                     headers={"Authorization": f"Bearer {self.token}"},
                                     data=billing_model.serialize())
            return response.json()
        except Exception as ex:
            return {}

    def request_search_billing(self, shipping: Shipping):
        self.token = self._request_authorize_token()
        try:
            response = requests.get(self.url + 'cob/' + shipping.TaxId,
                                    headers={"Authorization": f"Bearer {self.token}"})
            return response.json()
        except Exception as ex:
            return {}
