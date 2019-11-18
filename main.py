import os, threading, time
import win32gui
from logger import log
import pyautogui
pyautogui.FAILSAFE = True

#全局识别图片
class OverallFind(threading.Thread):
    def __init__(self, picture, text):
        super(OverallFind, self).__init__()
        self.picture = 'picture/overall/' + picture + '.png'
        self.text = text
    def run(self):
        while True:
            try:
                self.point = pyautogui.locateCenterOnScreen(self.picture, confidence=0.9)
                log.logger.warning(self.text)
                time.sleep(5)
            except TypeError:
                time.sleep(0.5)

#执行case文件夹下所有.py文件
class CaseMain(threading.Thread):
    def __init__(self):
        super(CaseMain, self).__init__()
    def run(self):
        lst = os.listdir('case')  
        for c in lst:
            if os.path.isfile('case/'+ c) and c.endswith('.py'):
                log.logger.info('执行'+ c)
                os.system(os.path.join(os.getcwd(),'case/'+ c))
        log.logger.info('所有case执行完成')

#调整窗口大小
def changeWindow():
    hwnd = win32gui.FindWindow(None,"优赢 - Google Chrome")
    try:
        win32gui.MoveWindow(hwnd,0,0,1600,860,True)
    except Exception:
       pass

if __name__ == '__main__':
    changeWindow()
    #全局识别 “系统错误”
    systemError = OverallFind('systemError', '发现\"系统错误\"！')
    # test = OverallFind('test', '发现\"商品出库库位必须选择\"！')
    allCase = CaseMain()

    systemError.start()
    # test.start()
    allCase.start()

