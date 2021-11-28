# 导入必须的库
import curses
import time

# 初始化命令行界面,返回的 stdscr 为窗口对象,表示命令行界面
stdscr = curses.initscr()

# 使用 noecho 方法关闭命令行回显
curses.noecho()
# 使用 nodelay(True) 方法让 getch 为非阻塞等待(即使没有输入程序也能继续执行)

stdscr.nodelay(True)
while True:
    try:
        strscr.erase()
    except:
        curses.endwin()
        break

# curses.wrapper(main)
