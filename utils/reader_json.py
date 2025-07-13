import json
import os

path = os.path.join("D:\\", "RokAutomation", "src", "json_file")

with open(os.path.join(path, "Accounts.json"), 'r') as account_reader:
    accounts = json.load(account_reader)

with open(os.path.join(path, "Settings.json"), 'r') as account_reader:
    setting = json.load(account_reader)

with open(os.path.join(path, "rightMenu.json"), 'r') as account_reader:
    rightmenu = json.load(account_reader)

with open(os.path.join(path, "City.json"), 'r') as account_reader:
    city = json.load(account_reader)
with open(os.path.join(path, "FiddleStick.json"), 'r') as account_reader:
    fiddle = json.load(account_reader)


