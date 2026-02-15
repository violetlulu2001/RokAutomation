import time

from utils.mouse_code import (change_city, join_rally)

if __name__ == '__main__':
    list_acc = [1, 2, 3, 4, 5, 6]
    for i in list_acc:
        change_city(i)
        time.sleep(5)
        join_rally()