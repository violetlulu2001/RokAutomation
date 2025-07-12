import os
from util_function import get_datetime_format

class OsFile:
    def __init__(self):
        self.path_file = os.path.join("G:", "logs", "violeta_logs")

    def create_folder(self)-> str | None:
        current_logs = os.path.join(self.path_file, get_datetime_format().split("_")[0])
        if not os.path.exists(current_logs):
            os.mkdir(current_logs)
        else:
            current_logs = os.path.join(current_logs, get_datetime_format().split("_")[-1])
            if not os.path.exists(current_logs):
                os.mkdir(current_logs)
                return current_logs


os_file = OsFile()