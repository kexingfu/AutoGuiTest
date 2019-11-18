from pyautogui import typewrite, hotkey
import time, os, sys
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from autoFunction import click, clickd, move, moved, scroll, write, writec, exist, dec

def testcase():
    
    moved(dx = 100, dy= 100)
    moved(dx = 100, dy= 100)
    scroll(-500)

if __name__ == '__main__':
    testcase()
