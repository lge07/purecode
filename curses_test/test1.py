#!/usr/bin/env python
import curses

scr = curses.initscr()
scr.keypad(0)
curses.noecho()

scr.addstr("hello world")
scr.refresh()
while True:
    a = scr.getch()
    scr.addstr(str(a)+"\n")
    if a==97:
        break

curses.endwin()