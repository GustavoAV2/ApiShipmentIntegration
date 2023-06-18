import requests
import json
from typing import Dict
from src.log import logger


class PixClient:
    def __init__(self):
        self.url = "http://localhost:8080/"
        self.token = ""
        self.client_id = "citiClientTest"
        self.client_secret = "citiClientTest"

    def _request_authorize_token(self):
        if self.token:
            return self.token
        try:
            payload = {"client_id": self.client_id, "client_secret": self.client_secret}
            response = requests.post(self.url + 'oauth/token', data=payload)
            return response
        except Exception as ex:
            return {}

    def request_create_cob(self, cob_data: Dict):
        self.token = self._request_authorize_token()
        try:
            # Implementação Pix API - Mockada
            # response = requests.post(self.url + 'cob', headers={"Authorization": f"Bearer {self.token}"},
            #                          data=cob_data)
            # return response
            with open("example_data/cob_example.json", 'r') as f:
                return {"status_code": 403, "data": json.loads(f.read())}

        except Exception as ex:
            logger.info(f"Erro: {ex.args}")
            return {"status_code": 403}

    def request_get_pix_payload(self, pix_url_access_token: str):
        self.token = self._request_authorize_token()
        try:
            url = self.url + pix_url_access_token
            logger.info("Requesição GET: " + url)
            response = requests.get(self.url,
                                    headers={"Authorization": f"Bearer {self.token}"})
            return response
        except Exception as ex:
            logger.info(f"Erro: {ex.args}")
            return {}

    @staticmethod
    def valid_response(response):
        if response.get("status_code") >= 400:
            return False
        return True
