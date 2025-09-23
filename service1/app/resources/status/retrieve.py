import logging
from flask import make_response
from app.resources.utils import Resource

logger = logging.getLogger(__name__)


class RetrieveStatusResource(Resource):
    def get(self):
        logger.info("RetrieveStatusResource GET request received")
        response = make_response("Status endpoint is working", 200)
        response.headers['Content-Type'] = 'text/plain'
        return response
