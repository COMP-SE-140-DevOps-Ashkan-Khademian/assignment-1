from .status import url_mapping as status_url_mapping
from .log import url_mapping as log_url_mapping

url_mapping = [
    *status_url_mapping,
    *log_url_mapping,
]
