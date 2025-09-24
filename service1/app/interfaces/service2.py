import requests

from flask import current_app


class Service2Interface:

    def __init__(self) -> None:
        self.base_url = current_app.config["SERVICE2_URL"]

    def get_status(self):
        response = requests.get(f"{self.base_url}/status")
        return response.text
