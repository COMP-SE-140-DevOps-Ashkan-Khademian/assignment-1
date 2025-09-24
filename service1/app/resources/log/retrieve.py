import logging
from app.resources.utils import Resource

logger = logging.getLogger(__name__)


class RetrieveLogResource(Resource):
    def get(self):
        logger.info("RetrieveLogResource GET request received")
        return self.make_plain_text_response("Log endpoint is working")
