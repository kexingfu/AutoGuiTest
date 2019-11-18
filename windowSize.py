import win32gui

hwnd = win32gui.FindWindow(None,"优赢 - Google Chrome")
# 没有直接修改窗口大小的方式，但可以曲线救国，几个参数分别表示句柄,起始点坐标,宽高度,是否重绘界面 ，如果想改变窗口大小，就必须指定起始点的坐标，没果对起始点坐标没有要求，随便写就可以；如果还想要放在原先的位置，就需要先获取之前的边框位置，再调用该方法即可
win32gui.MoveWindow(hwnd,0,0,1600,860,True)