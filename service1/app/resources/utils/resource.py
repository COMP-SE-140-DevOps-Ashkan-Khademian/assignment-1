from flask import make_response
from flask_restful import Resource as FlaskResource


class Resource(FlaskResource):

    def make_plain_text_response(
        self,
        text: str,
        status_code: int = 200,
        headers: dict | None = None,
    ):
        headers = headers or {}
        headers.update({"Content-Type": "text/plain"})
        response = make_response(text, status_code, headers)
        return response
