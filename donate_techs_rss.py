import os.path


from utils.reader_json import accounts
from utils.mouse_code import (change_city, donate_alliance_tech)

if __name__ == '__main__':
    count_accounts = accounts["Accounts_count"]["first_acc"]
    for i in range(1, count_accounts+1):
        change_city(i)
        donate_alliance_tech()
