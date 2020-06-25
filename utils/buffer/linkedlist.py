class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None
        self.prev = None
    
    def getData(self):
        return self.data
    
    def isStart(self):
        return self.prev == None
    
    def isEnd(self):
        return self.nxt == None

    def addInRear(self, node):
        """
        Adds node behind current node
        """
        if not self.isStart():
            pastPrev = self.prev
            pastPrev.nxt = node
            node.prev = pastPrev
        else:
            node.prev = None
        node.nxt = self
        self.prev = node
    
    def addInFront(self, node):
        """
        Adds node in front of current node
        """
        if not self.isEnd():
            pastNxt = self.nxt
            pastNxt.prev = node
            node.nxt = pastNxt
        else:
            node.nxt = None
        node.prev = self
        self.nxt = node
    
    def remove(self):
        """
        Removes node.
        """
        if not self.isStart():
            self.prev.nxt = self.nxt
        if not self.isEnd():
            self.nxt.prev = self.prev
        return self
        
class DoublyLinkedList:
    def __init__(self, seekintv: int):
        self.start = None
        self.end = None
        self.seeks = []
        self.seekintv = seekintv
        self.totalCount = 0
    
    def isEmpty(self):
        return (self.start == None)
    
    def Traverse(self, index: int = -1):
        """
        Iterates through the list and traverses to a position, or traverses through the entire list
        """
        if not self.isEmpty():
            ct = 0
            item = self.start
            while (item != None and ((ct <= index) or (index == -1))):
                yield item
                item = item.nxt
                ct += 1

    def revTraverse(self, index: int = -1):
        """
        Traverses the list in reverse and returns the Node
        """
        if not self.isEmpty():
            ct = self.totalCount
            item = self.end
            while (item != None and ((ct > index))):
                yield item
                item = item.prev
                ct -= 1

    def getIndex(self, index: int = -1):
        """
        Gets a specific element by using seeks and traversing in most efficient direction
        """
        if index == -1:
            return self.end
        else:
            interseek = index % self.seekintv
            seekct = int(abs(index - interseek) / self.seekintv)
            if interseek == 0:
                return self.seeks[seekct]
            elif interseek <= (self.seekintv / 2):
                # Closer to seek
                start = self.seeks[seekct]
                for x in range(interseek):
                    start = start.nxt
                return start
            elif interseek > (self.seekintv / 2):
                # Farther from seek
                start = self.seeks[seekct + 1]
                for x in range(interseek):
                    start = start.prev
                return start
    
    def append(self, data: any, index: int = -1):
        """
        Adds an item to the list at position ``index``. Default (-1) appends to end.
        """
        if self.isEmpty():
            self.totalCount +=1
            self.start = Node(data)
            self.start.prev = None
            self.seeks.append(self.start)
            self.end = self.start
        elif - 1 <= index < self.totalCount:
            self.totalCount +=1
            newNode = Node(data)
            item = self.getIndex(index)
            if index != -1:
                item.addInRear(newNode)
                if index == 0:
                    self.start = newNode
                ct = 0
                for seek in self.seeks:
                    if ct >= index and seek.prev != None:
                        self.seeks[ct] = seek.prev
                    ct += self.seekintv
            else:
                item.addInFront(newNode)
                self.end = newNode
            if self.getNewRequiredSeek():
                self.seeks.append(self.end)
    
    def delete(self, index: int = -1):
        """
        Deletes item at index. Default (-1) deletes at end.
        """
        if self.isEmpty():
            return
        elif -1 <= index < self.totalCount:
            self.totalCount -= 1
            item = self.getIndex(index)
            item.remove()
            ct = 0
            if index != -1:
                for seek in self.seeks:
                    if ct >= index and seek.nxt != None:
                        self.seeks[ct] = seek.nxt
                    ct += self.seekintv
            if self.getDelRequiredSeek():
                self.seeks.remove(self.end)
            if index == 0 or self.totalCount == 0:
                self.start = item.nxt
            elif index == -1 or index == self.totalCount:
                self.end = item.prev
            return item
        return
    
    def getNewRequiredSeek(self):
        return ((self.totalCount - 1) % self.seekintv == 0) and (len(self.seeks) < (self.totalCount + 1) / self.seekintv)
    
    def getDelRequiredSeek(self):
        return ((self.totalCount - 1) % self.seekintv != 0) and (len(self.seeks) > (self.totalCount + 1) / self.seekintv)