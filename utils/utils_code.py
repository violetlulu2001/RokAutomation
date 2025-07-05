import time
from reader_json import accounts, setting, rightmenu
import pyautogui


def change_city(i):
    pyautogui.click(setting['Profile']["x"], setting['Profile']["y"], duration=1)
    pyautogui.click(setting['Setting']["x"], setting['Setting']['y'], duration=1)
    pyautogui.click(setting['Account']['x'], setting['Account']['y'], duration=1)
    pyautogui.click(accounts[f'Bot{i}']['x'], accounts[f'Bot{i}']['y'], duration=1)
    pyautogui.click(accounts[f'Bot{i}']['x'], accounts[f'Bot{i}']['y'], duration=1)
    pyautogui.click(setting['Account_changer']['yes_btn_change_acc']['x'],
                    setting['Account_changer']['yes_btn_change_acc']['y'], duration=1)
    time.sleep(10)
    pyautogui.click(setting['Account_changer']['yes_btn_change_acc']['x'],
                    setting['Account_changer']['yes_btn_change_acc']['y'], duration=1)
    time.sleep(10)

def get_alliance_rss():
    pyautogui.click(rightmenu['Alliance']["location_btn"]['x'], rightmenu['Alliance']["location_btn"]['y'], duration=1)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["location_btn"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["location_btn"]['y'], duration=1)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["claim"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["claim"]['y'], duration=1)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['y'], duration=1)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['y'], duration=1)
