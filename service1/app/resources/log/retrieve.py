import logging
from flask import make_response
from app.resources.utils import Resource

logger = logging.getLogger(__name__)


class RetrieveLogResource(Resource):
    def get(self):
        logger.info("RetrieveLogResource GET request received")
        response = make_response("Log endpoint is working", 200)
        response.headers['Content-Type'] = 'text/plain'
        return response
