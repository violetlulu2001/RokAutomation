import os
import time
from reader_json import accounts, setting, rightmenu, city
import pyautogui


def join_rally() -> None:
    pyautogui.click(city['castle']['location']['lvl_25']["x"], city['castle']['location']['lvl_25']["y"], duration=2)
    pyautogui.click(city['castle']['rally_btn']["x"], city['castle']['rally_btn']["y"], duration=2)
    time.sleep(5)
    try:
        button7location = pyautogui.locateOnScreen('D:\\RokAutomation\\src\\image\\profile_main.png', confidence=0.9)
        button7location = pyautogui.center(button7location)
        pyautogui.click(button7location.x, button7location.y, duration=2)
    except Exception as e:
        print(e)
    pyautogui.click(city['castle']['join_rally']["x"], city['castle']['join_rally']["y"], duration=2)
    pyautogui.click(city['castle']['new_troops']["x"], city['castle']['new_troops']["y"], duration=2)
    pyautogui.click(city['castle']['march_troops']["x"], city['castle']['march_troops']["y"], duration=2)





def start_blacksmith(mat:str) -> None:
    pyautogui.click(city['blacksmith']['location']["x"], city['blacksmith']['location']["y"], duration=1)
    pyautogui.click(city['blacksmith']['craft_mats']['location']["x"], city['blacksmith']['craft_mats']['location']["y"], duration=1)
    pyautogui.click(city['blacksmith']['craft_mats'][mat]["x"], city['blacksmith']['craft_mats'][mat]["y"], clicks=5, duration=4,
                    interval=1)
    pyautogui.click(city['blacksmith']['close_btn']["x"], city['blacksmith']['close_btn']["y"], duration=1)


def change_city(i:int) -> None:
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
    time.sleep(15)

def get_alliance_rss() -> None:
    pyautogui.click(rightmenu['Alliance']["location_btn"]['x'], rightmenu['Alliance']["location_btn"]['y'], duration=1)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["location_btn"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["location_btn"]['y'], duration=1)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["claim"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["claim"]['y'], duration=1)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['y'], duration=1)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['y'], duration=1)

def get_daily_vip_and_ghs() -> None:
    pyautogui.click(setting["vip_btn"]["location_btn"]['x'], setting["vip_btn"]["location_btn"]['y'], duration=2)
    pyautogui.click(setting["vip_btn"]["vip_chest"]['x'], setting["vip_btn"]["vip_chest"]['y'], duration=2)
    pyautogui.click(setting["vip_btn"]["vip_chest"]['x'], setting["vip_btn"]["vip_chest"]['y'], duration=2)
    pyautogui.click(setting["vip_btn"]["gh_chest"]['x'], setting["vip_btn"]["gh_chest"]['y'], duration=2)
    pyautogui.click(setting["vip_btn"]["gh_chest"]['x'], setting["vip_btn"]["gh_chest"]['y'], duration=2)
    pyautogui.click(setting["vip_btn"]["close_btn_vip"]['x'], setting["vip_btn"]["close_btn_vip"]['y'], duration=2)

def donate_alliance_tech() -> None:
    pyautogui.click(rightmenu['Alliance']["location_btn"]['x'], rightmenu['Alliance']["location_btn"]['y'], duration=2)

    pyautogui.click(rightmenu['Alliance']['Alliance_list']['technology']["location_btn"]['x'],
                    rightmenu['Alliance']['Alliance_list']['technology']["location_btn"]['y'], duration=4)
    time.sleep(10)
    try:
        button7location = pyautogui.locateOnScreen('D:\\RokAutomation\\src\\image\\star_technology.png', confidence=0.9)
        button7location = pyautogui.center(button7location)
        print(button7location.x, button7location.y)
        pyautogui.click(button7location.x, button7location.y + 30, duration=2)
    except Exception as e:
        print(e)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['technology']["donate_btn"]['x'],
                    rightmenu['Alliance']['Alliance_list']['technology']["donate_btn"]['y'], clicks=20, duration=10,
                    interval=0.5)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['y'], duration=2)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['y'], duration=2)
    pyautogui.click(rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['x'],
                    rightmenu['Alliance']['Alliance_list']['territory']["close_teritory"]['y'], duration=2)

def find_stone() -> None:
    stone_imgs = "D:\\RokAutomation\\src\\image\\stone"
    for i in range(1, len(os.listdir(stone_imgs))+1):
        try:
            button7location = pyautogui.locateOnScreen(f'D:\\RokAutomation\\src\\image\\stone\\stone{i}.png', confidence=0.9)
            button7location = pyautogui.center(button7location)
            print(button7location.x, button7location.y)
            pyautogui.click(button7location.x, button7location.y + 30, duration=2)
        except Exception as e:
            print(e)


