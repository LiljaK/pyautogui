import pyautogui as pg
import time
pg.hotkey ("winleft","ctrl","d")
pg.hotkey ("winleft")
pg.typewrite ("chrome\n",.1)
pg.hotkey ("winleft", "up")
pg.typewrite ("netflix.com\n", .5)
time.sleep(2)
pg.hotkey ('tab')
pg.hotkey ('tab')
pg.hotkey ("enter")
time.sleep (1)
pg.hotkey ("tab")
pg.typewrite ("lkjaernested@gcds.net",.2)
pg.hotkey ('tab')
pw=pg.password('Enter password here','Password box','','*')
pg.typewrite(pw+"\n", 0.3)
pw = ""
