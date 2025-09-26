from flask import request

from app.services import FileDBService
from app.resources.utils import Resource


class CreateLogResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.db_service = FileDBService()

    def post(self):
        log = request.get_data(as_text=True) or ""
        if not log.strip():
            return self.make_plain_text_response("Log message is required", 400)
        self.db_service.append_data(log)
        return self.make_plain_text_response(log, 201)
