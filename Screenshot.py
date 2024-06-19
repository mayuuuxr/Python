import pyautogui
import time

def SS():
    time.sleep(2)
    name = time.time()
    name = 'G:/ex_py/new/ADv/ss/{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

SS()    