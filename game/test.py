import sys
import pygame as pg

pg.init()

# main window
screen = pg.display.set_mode((640, 480))
face = pg.Surface((100, 100), flags=pg.HWSURFACE)
face.fill(color='yellow')
screen.blit(face, (100, 100))

# f = pg.font.Font()


# 固定代码段,实现点击"X"号退出界面的功能,几乎所有的pg都会使用该段代码
while True:
    # 循环获取事件,监听事件状态
    for event in pg.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pg.QUIT:
            #卸载所有模块
            pg.quit()
            #终止程序,确保退出程序
            sys.exit()
    pg.display.flip() #更新屏幕内容