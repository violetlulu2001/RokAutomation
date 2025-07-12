import logging
from os_zone import os_file
import os
from util_function import get_datetime_format


class LoggerServer:
    def __init__(self, name:str):
        self.name = name
        file_path = os_file.create_folder()
        file_path = os.path.join(file_path, self.name)
        logging.basicConfig(filename=f"{file_path}_{get_datetime_format().split("_")[-1]}_{self.name}.logs",
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            filemode='w')

        self.logger = logging.getLogger(self.name)

        self.logger.setLevel(logging.DEBUG)


    def debug_writer(self, text):
        self.logger.debug(text)

    def info_writer(self, text):
        self.logger.info(text)
    
    def error_writer(self, text):
        self.logger.error(text)
