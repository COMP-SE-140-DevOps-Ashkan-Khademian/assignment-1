import logging

from app.interfaces import StorageInterface
from app.resources.utils import Resource

logger = logging.getLogger(__name__)


class RetrieveLogResource(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.storage = StorageInterface()
    
    def get(self):
        logs: str = self.storage.get_logs()
        return self.make_plain_text_response(logs)
