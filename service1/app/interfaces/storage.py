import requests

from flask import current_app as app


class StorageInterface:

    def __init__(self) -> None:
        self.base_url = app.config["STORAGE_URL"]

    def get_logs(self) -> str:
        response = requests.get(f"{self.base_url}/log")
        response.raise_for_status()
        return response.text

    def append_log(self, log_entry: str) -> None:
        headers = {"Content-Type": "text/plain"}
        response = requests.post(
            f"{self.base_url}/log", data=log_entry.encode("utf-8"), headers=headers
        )
        response.raise_for_status()
