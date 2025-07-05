from reader_json import accounts
from utils.utils_code import change_city, get_alliance_rss


if __name__ == '__main__':
    count_accounts = accounts["Accounts_count"]["first_acc"]
    for i in range(1, count_accounts+1):
        change_city(i)
        get_alliance_rss()