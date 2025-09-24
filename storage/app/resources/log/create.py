import logging
from flask_restful import reqparse, fields

from app.services import FileDBService
from app.resources.utils import Resource

logger = logging.getLogger(__name__)


class CreateLogResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.db_service = FileDBService()
        self.log_parser = reqparse.RequestParser()
        self.log_parser.add_argument(
            "log", type=str, required=True, help="Log message is required"
        )

    def post(self):
        args = self.log_parser.parse_args()
        log = args["log"]
        self.db_service.append_data(log)
        return {"log": log, "message": "created"}, 201
