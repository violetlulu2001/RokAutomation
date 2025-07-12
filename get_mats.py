from reader_json import accounts
from utils.mouse_code import (change_city,
                              start_blacksmith)

if __name__ == 'get_mats':
    count_accounts = accounts["Accounts_count"]["first_acc"]
    for i in range(1, count_accounts+1):
        change_city(i)
        start_blacksmith('bone')