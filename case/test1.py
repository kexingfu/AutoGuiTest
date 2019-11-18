from pyautogui import typewrite, hotkey
import time, os, sys
parentdir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0,parentdir)
from autoFunction import click, clickd, move, moved, scroll, write, writec, exist, dec, drag
from otherFunction import excuteCase

def testcase():
    excuteCase('createSaleOrder')
    excuteCase('test2')
    click('addgoods', dt =1)
    moved(dx = 100, dy= 100)
    moved(dx = 100, dy= 100)
    scroll(-500)

if __name__ == '__main__':
    testcase()
