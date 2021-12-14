import curses
import time

def init(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    curses.curs_set(0)

def end(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.curs_set(1)
    curses.endwin()


def main(stdscr):
    while True:
        # win = curses.newwin(5, 5, 0, 0)
        # stdscr.clear()
        try:
            key = stdscr.getkey()

            stdscr.addstr(0, ord(key) - ord('a'), key)
        except Exception as e:
            # print(e)
            pass
        # time.sleep(0.01)
        stdscr.refresh()

stdscr = curses.initscr()
init(stdscr)
try:
    main(stdscr)
except KeyboardInterrupt:
    end(stdscr)

