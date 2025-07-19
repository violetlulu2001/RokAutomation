from utils.mouse_code import (change_city, join_rally, change_acct)

if __name__ == '__main__':
    list_acc = [6,7]
    for i in list_acc:
        change_city(int(i))
        join_rally()
    change_acct()
    list_acc = [2, 3]
    for i in list_acc:
        change_city(int(i))
        join_rally()
    change_acct()