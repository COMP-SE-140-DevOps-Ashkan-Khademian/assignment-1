import logging
from app.interfaces import Service2Interface
from app.services import StatusService
from app.resources.utils import Resource

logger = logging.getLogger(__name__)


class RetrieveStatusResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.service2 = Service2Interface()
        self.status_service = StatusService()

    def get(self):
        logger.info("RetrieveStatusResource GET request received")
        my_status = self.status_service.get_status()
        service2_status = self.service2.get_status()
        response_text = f"{my_status}\n{service2_status}"
        return self.make_plain_text_response(response_text)
