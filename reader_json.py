import json
import os

path = os.path.join("RokAutomation", "src", "json_file")
path = f'F:\\{path}'

with open(os.path.join(path, "Accounts.json"), 'r') as account_reader:
    accounts = json.load(account_reader)

with open(os.path.join(path, "Settings.json"), 'r') as account_reader:
    setting = json.load(account_reader)

with open(os.path.join(path, "rightMenu.json"), 'r') as account_reader:
    rightmenu = json.load(account_reader)

with open(os.path.join(path, "City.json"), 'r') as account_reader:
    city = json.load(account_reader)
