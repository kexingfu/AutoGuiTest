import pyautogui, pyperclip
import time, os, sys
import settings
from logger import log

#通过图片名获取图片路径
def getPath(fileName, imgType):

    fullBase = os.path.basename(sys.argv[0])
    base = os.path.splitext(fullBase)[0]
    isfile = None
    if(os.path.exists('picture/' + base)):
        isfile = os.path.exists('picture/' + base + '/' + fileName + '.' + imgType)
    if(isfile):
        return 'picture/' + base + '/' + fileName + '.' + imgType
    else:
        return 'picture/' + 'common' + '/' + fileName + '.' + imgType
            
#移动到图片位置
def move(fileName, dx=0, dy=0, dt=0, imgType=settings.imageType, dur=settings.moveDuration, maxloop= settings.maxloop, maxloopExit= settings.maxloopExit):
    pic = getPath(fileName, imgType)
    if(dt!=0):
        time.sleep(dt)
    isfind = False
    firstrun = True
    while(not isfind and maxloop):
        try:
            maxloop -= 1
            x,y = pyautogui.locateCenterOnScreen(pic, confidence=settings.moveConfidence, grayscale=settings.grayscale)
            isfind = True
        except TypeError:
            if(firstrun):
                log.logger.info('没有找到图片'+ pic + ', 重试中。')
                firstrun = False
            if(maxloop<=0):
                if(maxloopExit):
                    log.logger.warning('没有找到图片'+ pic + ', 退出case。' )
                    os._exit(0)
                else:
                    log.logger.warning('没有找到图片'+ pic + ', 继续执行。' )
                    return False
        else:
            pyautogui.moveTo(x+dx, y+dy, duration=dur)
            return True

#点击图片位置
def click(fileName, dx=0, dy=0, dt=0, imgType=settings.imageType,dur=settings.clickDuration, maxloop= settings.maxloop, maxloopExit= settings.maxloopExit):
    pic = getPath(fileName, imgType)
    if(dt!=0):
        time.sleep(dt)
    isfind = False
    firstrun = True
    while(not isfind and maxloop):
        try:
            maxloop -= 1
            x,y = pyautogui.locateCenterOnScreen(pic, confidence=settings.clickConfidence, grayscale=settings.grayscale)
            isfind = True
        except TypeError:
            if(firstrun):
                log.logger.info('没有找到图片'+ pic + ', 重试中。')
                firstrun = False
            if(maxloop<=0):
                if(maxloopExit):
                    log.logger.warning('没有找到图片'+ pic + ', 退出case。' )
                    os._exit(0)
                else:
                    log.logger.warning('没有找到图片'+ pic + ', 继续执行。' )
                    return False
        else:
            pyautogui.click(x+dx, y+dy, duration=dur)
            return True

#鼠标相对移动
def moved(dx = 0, dy = 0, dur=settings.moveDuration):
    pyautogui.moveRel(dx ,dy, duration=dur)

#输入文字
def write(inputstr):
    pyautogui.typewrite(str(inputstr))

#使用粘贴方法输入（可输入中文）
def writec(inputstr):
    pyperclip.copy(inputstr)
    pyautogui.hotkey('ctrl', 'v')

#滚轮
def scroll(distance):
    pyautogui.scroll(distance)

#从图片位置拖拽到目标位置
def drag(fileName, gx, gy, dx=0, dy=0, dt=0, imgType=settings.imageType,dur=settings.dragDuration, rel=False, maxloop= settings.maxloop, maxloopExit= settings.maxloopExit):
    pic = getPath(fileName, imgType)
    if(dt!=0):
        time.sleep(dt)
    isfind = False
    firstrun = True
    while(not isfind and maxloop):
        try:
            maxloop -= 1
            x,y = pyautogui.locateCenterOnScreen(pic, confidence=settings.moveConfidence, grayscale=settings.grayscale)
            isfind = True
        except TypeError:
            if(firstrun):
                log.logger.info('没有找到图片'+ pic + ', 重试中。')
                firstrun = False
            if(maxloop<=0):
                if(maxloopExit):
                    log.logger.warning('没有找到图片'+ pic + ', 退出case。' )
                    os._exit(0)
                else:
                    log.logger.warning('没有找到图片'+ pic + ', 继续执行。' )
                    return False
        else:
            pyautogui.moveTo(x+dx, y+dy, duration=dur)
            if(not rel):
                pyautogui.dragTo(gx,gy,duration=settings.dragDuration)
                return True
            else:
                pyautogui.dragRel(gx,gy,duration=settings.dragDuration)
                return True

#鼠标相对点击
def clickd(dx = 0, dy = 0, dt = 0, button='left', dur=settings.moveDuration):
    if(dt!=0):
        time.sleep(dt)
    pyautogui.moveRel(dx ,dy , duration=dur)
    pyautogui.click(button=button)

#检测图片是否存在，存在再进行下一步
def exist(fileName, imgType=settings.imageType):
    pic = getPath(fileName, imgType)
    isfind = False
    firstrun = True
    while(not isfind):
        try:
            pyautogui.locateCenterOnScreen(pic, confidence=settings.clickConfidence, grayscale=settings.grayscale)
            isfind = True
        except TypeError:
            if(firstrun):
                log.logger.info('没有找到图片'+ pic + ', 重试中。')
                firstrun = False
        else:
            return True

#断言
def dec(fileName, falseText = '', successText = '', dt=0, imgType=settings.imageType, maxloop=0):
    pic = getPath(fileName, imgType)
    isfind = False
    if(dt!=0):
        time.sleep(dt)
    while(not isfind):
        try:
            if(not maxloop):
                pyautogui.locateCenterOnScreen(pic, confidence=settings.clickConfidence, grayscale=settings.grayscale)
                log.logger.info('断言成功。'+ str(successText))
                isfind = True
                return True
            else:
                maxloop -= 1
                pyautogui.locateCenterOnScreen(pic, confidence=settings.clickConfidence, grayscale=settings.grayscale)
                log.logger.info('断言成功。'+ str(successText))
                isfind = True
                return True
        except TypeError:
            if(maxloop<=0):
                log.logger.warning('断言失败。'+ str(falseText))
                return False

#获取一张截图并命名存在本地
def shot(fileName, x, y, w, h):
    fullBase = os.path.basename(sys.argv[0])
    base = os.path.splitext(fullBase)[0]
    filePath = None
    if(os.path.exists('picture/' + base)):
        filePath = 'picture/' + base 
    else:
        filePath = 'picture/' + 'common'
    return pyautogui.screenshot(filePath + '/' + fileName + '.png', region=(x, y, w, h))