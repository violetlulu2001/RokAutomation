from reader_json import accounts
from utils.utils_code import (change_city, get_alliance_rss, get_daily_vip_and_ghs, donate_alliance_tech, find_stone,
                              start_blacksmith, join_rally)

if __name__ == '__main__':
    count_accounts = accounts["Accounts_count"]["first_acc"]
    for i in range(1, count_accounts+1):
        change_city(i)
        #     get_alliance_rss()
        #     get_daily_vip_and_ghs()
        donate_alliance_tech()
        # # find_stone()
        #     start_blacksmith('bone')
        # join_rally()
