###基于pyautogui的纯ui自动化测试框架###


## 目录结构 ##

--baseCase
  |-
--case
  |-
--main.py

*执行main文件,将执行case文件夹下所有py文件，case文件夹下的文件可调用baseCase文件夹下的文件，也可以直接写用例
*case、baseCase 文件夹下编写的用例可单独执行
*settings.py 可配置一些函数的默认参数、日志打印级别参数等
*runTestCase.log 为执行后生成的日志


## 图片目录 ##
图片优先找picture目录下同case名目录（代码写在的那个文件的名字），如果目录不存在或者目录中无目标文件，则在picture目录下的common目录下找


## 可用函数 ##

# 执行一个baseCase文件夹下的文件
excuteCase(name)
excuteCase(文件名)

# 移动到图片位置move
move(fileName, dx=0, dy=0, dt=0, imgType=settings.imageType,dur=settings.moveDuration, maxloop= settings.maxloop, maxloopExit= settings.maxloopExit)
move(图片名, 水平偏移量, 竖直偏移量, 延迟多少时间再移动, 图片格式, 鼠标移动时间, 最大查找次数, 到达最大查找次数后是否退出)

# 点击图片位置click
click(fileName, dx=0, dy=0, dt=0, imgType=settings.imageType,dur=settings.clickDuration, maxloop= settings.maxloop, maxloopExit= settings.maxloopExit)
click(图片名, 水平偏移量, 竖直偏移量, 延迟多少时间再点击, 图片格式, 鼠标移动时间, 最大查找次数, 到达最大查找次数后是否退出)

# 鼠标相对自己的位置移动到一个点
moved(dx = 0, dy = 0, dur=settings.moveDuration)
moved(水平偏移量, 竖直偏移量, 鼠标移动时间)

# 输入字符
write(inputstr)
write(需要输入的字符串[不支持中文])

# 使用粘贴方法输入（可输入中文）
writec(需要输入的字符串)
writec(需要输入的字符串)

# 滚轮
scroll(distance)
scroll(滚动的像素[正负控制向上向下])

# 从图片位置拖拽到目标位置 (或相对位置，由参数 rel 控制)
drag(fileName, gx, gy, dx=0, dy=0, dt=0, imgType=settings.imageType,dur=settings.dragDuration, rel=False, maxloop= settings.maxloop, maxloopExit= settings.maxloopExit)
drag(图片名, 目标位置x坐标[或相对位置的水平方向移动距离], 目标位置y坐标[或相对位置的竖直方向移动距离] ,水平偏移量, 竖直偏移量, 延迟多少时间再移动, 图片格式, 鼠标移动时间, 是否相对拖拽, 最大查找次数, 到达最大查找次数后是否退出)

# 鼠标相对自己的位置移动到一个点并点击
clickd(dx = 0, dy = 0, dt = 0, button='left', dur=settings.moveDuration)
clickd(水平偏移量, 竖直偏移量, 延迟多少时间再移动, 点击左键还是右键, 鼠标移动时间)

# 检测图片是否存在，存在再进行下一步，不存在则一直检测
exist(fileName, imgType=settings.imageType)
exist(图片名, 图片格式)

# 断言 [检测一张图片是否存在，不存在则报错，存在则通过]
dec(fileName, falseText = '', successText = '', dt=0, imgType=settings.imageType, maxloop=0)
dec(图片名, 图片不存在时需要报的内容, 图片存在时需要报的内容, 延迟多少时间再断言, 图片格式, 最大查找次数[找多少次没找到则相当于失败，默认为1次])

# 获取一张截图并命名存在本地
shot(fileName, x, y, w, h)
shot(命名的文件名, 起始点x坐标, 起始点y坐标, 图片宽度, 图片高度)


## 全局识别 ##
main文件下，使用图片名、报错文字实例化OverallFind类，并.start开启一个线程即可 (可以开启多个线程全局识别多张图片)

##问题##
方法、函数未封装，很散，待整理
断言、批量执行应使用成熟的库：pytest等