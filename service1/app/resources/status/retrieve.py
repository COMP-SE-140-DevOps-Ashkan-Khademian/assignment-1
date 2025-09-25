from app.interfaces import Service2Interface, StorageInterface
from app.services import StatusService
from app.resources.utils import Resource


class RetrieveStatusResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.service2 = Service2Interface()
        self.status_service = StatusService()
        self.storage = StorageInterface()

    def get(self):
        my_status = self.status_service.get_status()
        self.storage.append_log(my_status)
        service2_status = self.service2.get_status()
        response_text = f"{my_status}\n{service2_status}"
        return self.make_plain_text_response(response_text)
