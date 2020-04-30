# Defines the bottom bar
import curses

class bottomBar:
    def __init__(self):
        self.bar = curses.newwin(3, curses.COLS - 1, curses.LINES - 3, 0)
        self.bar.box()
        self.bar.addstr(1, 1, "purecode::")
        self.lrAlloc = 5
        self.prevStr = ""
        self.bar.refresh()
    def addCentralStr(self, st):
        self.prevStr = st
        self.bar.addstr(1,11,(" "*(curses.COLS-11-self.lrAlloc)))
        self.bar.addstr(1, 11, str(st)[0: curses.COLS - 11 - self.lrAlloc])
        self.bar.refresh()
    def addLineRow(self, x, y):
        add = str(x) + "," + str(y)
        if len(add)>=self.lrAlloc:
            self.lrAlloc = len(add)
            self.addCentralStr(self.prevStr)
        self.bar.addstr(1, curses.COLS - self.lrAlloc, add)
        self.bar.refresh()