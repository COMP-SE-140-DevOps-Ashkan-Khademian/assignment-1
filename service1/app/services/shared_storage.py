from flask import current_app as app


class SharedStorageService:
    def __init__(self):
        self.file_path: str = app.config["SHARED_STORAGE_PATH"]

    def append(self, line: str) -> None:
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(f"{line}\n")
