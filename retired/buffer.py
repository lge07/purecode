# Eventually, the Buffer class will require significant speed improvements.
# For now, this should be alright.

class Buffer:
    def __init__(self, name: str):
        self.Lines = []
        self.name = name
    
    def getLines(self, xrange: tuple = (-1, -1), yrange: tuple = (-1, -1)):
        if yrange!=(-1,-1):
            ret = self.Lines[yrange[0] : yrange[1]]
        else:
            ret = self.Lines
        if xrange!=(-1,-1):
            ret = [x[xrange[0] : xrange[1]] for x in ret]
        else:
            pass
        return ret
    
    def modifyLine(self, text: str, xpos: int = 0, line: int = -1):
        if line == -1:
            line = len(self.getLines())
        if line not in range(0, len(self.Lines) - 1):
            self.Lines.insert(xpos, "")
        bf = self.Lines[line][0:xpos]
        aft = self.Lines[line][xpos: len(self.Lines)]
        self.Lines[line] = bf + text + aft
    
    def delLine(self, xrange: tuple = (-1, -1), yrange: tuple = (-1, -1)):
        if yrange == (-1, -1):
            yrange = (0, len(self.Lines) - 1)
        for l in range(yrange[0], yrange[1]):
            if xrange == (-1, -1):
                tmpxrange = (0,len(self.Lines[l]))
            self.Lines[l] = self.Lines[l][xrange[0] : xrange[1]]


    def massModify(self, lines: list):
        self.Lines = lines
    
    def getName(self):
        return self.name

    