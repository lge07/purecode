# The Code Scrapyard
# dll.py, under LinkedList class
def getAffectedSeeks(self, changePos: int):
        ret = []
        ct = 0
        for seek in self.seeks:
            if ct >= changePos:
                ret.append(seek)
            ct += self.seekintv
        return ret
    
    def getNewRequiredSeek(self):
        return ((self.totalCount - 1) % self.seekintv == 0) and (len(self.seeks) < (self.totalCount + 1) / self.seekintv)
    
    def getDelRequiredSeek(self):
        return ((self.totalCount - 1) % self.seekintv != 0) and (len(self.seeks) > (self.totalCount + 1) / self.seekintv)