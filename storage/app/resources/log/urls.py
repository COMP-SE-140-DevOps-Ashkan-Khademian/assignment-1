from .create import CreateLogResource
from .retrieve import RetrieveLogResource

url_mapping = [
    (CreateLogResource, "/log/"),
    (RetrieveLogResource, "/log/"),
]
