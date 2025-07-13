import os
from utils.util_function import get_datetime_format

class OsFile:
    def __init__(self):
        self.path_file = os.path.join("D:\\", "logs", "violeta_logs")

    def create_folder(self)-> str | None:
        current_logs = os.path.join(self.path_file, get_datetime_format().split("_")[-1])
        return current_logs


os_file = OsFile()