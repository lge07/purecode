import curses
import time
from bar import bottomBar


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
for y in range(0, curses.LINES - 2):
    stdscr.addstr(y,0,str(y))
    stdscr.refresh()
bar = bottomBar()

currLine = 0
currRow = 0
while True:
    stdscr.move(currRow,currLine)
    c = stdscr.getkey()
    bar.addCentralStr(c)
    g = stdscr.getbegyx()
    bar.addLineRow(currLine,currRow)
    if c == "KEY_A2" and currRow!=0:
        currRow -= 1
    if c == "KEY_C2" and currRow!=curses.LINES-4:
        currRow += 1
    if c == "^C":
        break
    stdscr.refresh()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()