import os
from utils.reader_json import accounts
from utils.mouse_code import (change_city, start_blacksmith)

from utils.os_zone import os_file
from utils.constants import name_mat, delimtator
from utils.util_function import get_datetime_format


if __name__ == '__main__':
    count_accounts = accounts["Accounts_count"]["first_acc"]
    path_file = os_file.create_folder()
    path_file: str = os.path.join(path_file, name_mat)
    with open(f'{path_file}_{get_datetime_format().split("_")[-1]}.txt', 'a') as writer:
        for i in range(1, count_accounts+1):
            change_city(i, writer)
            start_blacksmith('bone')