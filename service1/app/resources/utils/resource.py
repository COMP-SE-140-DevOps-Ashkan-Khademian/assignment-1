from typing import List
from functools import cached_property

from flask import request, make_response
from flask_restful import Resource as FlaskResource

from .request import RequestParams


class Resource(FlaskResource):

    @cached_property
    def request(self):
        return request

    @cached_property
    def params(self):
        return RequestParams(self.request)

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
