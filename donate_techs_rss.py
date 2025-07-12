from reader_json import accounts
from utils.mouse_code import (change_city, get_alliance_rss, get_daily_vip_and_ghs, donate_alliance_tech, find_stone,
                              start_blacksmith, join_rally)
from utils.logs_creater import LoggerServer
if __name__ == '__main__':
    count_accounts = accounts["Accounts_count"]["first_acc"]
    obj_loggin = LoggerServer("Donate_rss.py")
    for i in range(1, count_accounts+1):
        obj_loggin.debug_writer(f"Changing account Lulu{i}")
        change_city(i)
        obj_loggin.debug_writer(f"Successfully account changed to {i}")
        obj_loggin.debug_writer(f"Start Donate Tech in Lulu{i}")

        donate_alliance_tech()
        obj_loggin.debug_writer(f"Successfully Donate Tech in  Lulu{i}")

