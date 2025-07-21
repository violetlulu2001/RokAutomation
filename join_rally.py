import time

from utils.mouse_code import (change_city, join_rally)

if __name__ == '__main__':
    list_acc = [2, 3]
    for i in list_acc:
        change_city(int(i))
        time.sleep(1)
        join_rally()