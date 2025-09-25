import requests

from flask import current_app


class StorageInterface:

    def __init__(self) -> None:
        self.base_url = current_app.config["STORAGE_URL"]

    def get_logs(self) -> str:
        response = requests.get(f"{self.base_url}/log/")
        response.raise_for_status()
        return response.json()["logs"]

    def append_log(self, log_entry: str) -> None:
        response = requests.post(f"{self.base_url}/log/", json={"log": log_entry})
        response.raise_for_status()
