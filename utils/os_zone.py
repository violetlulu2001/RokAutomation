import os
from utils.util_function import get_datetime_format

class OsFile:
    def __init__(self):
        self.path_file = os.path.join("D:\\", "logs", "violeta_logs")

    def create_folder(self)-> str | None:
        return self.path_file


os_file = OsFile()