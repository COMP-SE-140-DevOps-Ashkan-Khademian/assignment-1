from flask import current_app as app


class FileDBService:

    def __init__(self) -> None:
        self.file_path = app.config["FILE_DB_PATH"]

    def exists(self) -> bool:
        import os

        return os.path.exists(self.file_path)

    def read_data(self) -> str:
        with open(self.file_path, "r") as file:
            data = file.read()
        return data

    def append_data(self, new_data):
        with open(self.file_path, "a") as file:
            file.write(new_data + "\n")

    def create_file(self):
        with open(self.file_path, "w") as file:
            file.write("")
