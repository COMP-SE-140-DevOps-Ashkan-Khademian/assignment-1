from app.services import FileDBService
from app.resources.utils import Resource


class RetrieveLogResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.db_service = FileDBService()

    def get(self):
        if not self.db_service.exists():
            self.db_service.create_file()

        data = self.db_service.read_data()
        return {"logs": data}, 200
