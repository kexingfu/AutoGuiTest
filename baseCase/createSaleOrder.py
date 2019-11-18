from pyautogui import typewrite, hotkey
import time, os, sys
parentdir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0,parentdir)
from autoFunction import click, clickd, move, moved, scroll, write, writec, exist, dec, drag, shot

def testcase():

    move('xiaoshou', dx = 0, dy= -15)
    click('saleorder')
    exist('totaldata')
    click('create')
    click('wldx')
    writec("123")
    clickd(dy=40,dt=0.5)
    click('addgoods')
    time.sleep(0.2)
    typewrite(['enter','down','enter'], '0.25')
    drag('orderSlider',500,0,dy=-8,rel=True)

    if(not dec('wldx',maxloop=5)):
        exit()
    shot('456',0,0,600,500)

if __name__ == '__main__':
    testcase()