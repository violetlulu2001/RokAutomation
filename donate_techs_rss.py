import os.path


from utils.reader_json import accounts
from utils.mouse_code import (change_city, donate_alliance_tech)
from utils.os_zone import os_file
from utils.constants import name_donate, delimtator
from utils.util_function import get_datetime_format

if __name__ == '__main__':
    count_accounts = accounts["Accounts_count"]["first_acc"]
    path_file = os_file.create_folder()
    path_file: str = os.path.join(path_file, name_donate)

    with open(f'{path_file}.txt', 'a') as writer:
        for i in range(1, count_accounts+1):
            writer.write(f'[{get_datetime_format().split("_")[-1]}] - {name_donate}.py | Changed account Lulu{i}\n')
            writer.write(delimtator)
            change_city(i, writer)
            writer.write(delimtator)
            writer.write(f'[{get_datetime_format().split("_")[-1]}] - {name_donate}.py | Donate Alliance Techs Lulu{i}\n')
            donate_alliance_tech(writer)
