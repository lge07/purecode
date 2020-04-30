import os

class Buffer:
    def __init__(self, body: str):
        self.file = body.split("\n")

    def get(self, xrange: tuple, yrange: tuple) -> str:
        ret = self.file[yrange[0] : yrange[1]]
        ret = [x[xrange[0] : xrange[1]] for x in ret]
        return ret

    def modify(self,text: str, xrange: tuple, yrange:tuple)