def cutSeg(self, fromPos: int, toPos: int):
        """
        Traverses to position, cuts off component of list, returns
        TODO: Add support for the end/start -1 and -2
        """
        start = self.getIndex(fromPos)
        end = self.getIndex(toPos)
        ret = deepcopy(start)
        start.addInFront(end)

    def addSeg(self, cut: Node, pos: int):
        """
        Inserts cut segment at position
        TODO: Add support for the end/start -1 and -2
        """
        if pos == -2:
            tmpstart = self.start
            self.start = cut
        else:
            start = self.getPos(pos)
            tmpnxt = start.nxt
            start.nxt = cut
            tmp = cut
            while tmp.nxt != None:
                tmp = tmp.nxt
            tmp.nxt = tmpnxt