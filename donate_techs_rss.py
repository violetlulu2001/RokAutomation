from utils.reader_json import accounts
from utils.mouse_code import (change_city, donate_alliance_tech, change_acct)

if __name__ == '__main__':
    count_accounts = accounts["Accounts_count"]["second_acc"]
    for i in range(1, count_accounts+1):
        change_city(i)
        donate_alliance_tech()
    change_acct()
    count_accounts = accounts["Accounts_count"]["first_acc"]
    for i in range(1, count_accounts + 1):
        change_city(i)
        donate_alliance_tech()
    change_acct()

