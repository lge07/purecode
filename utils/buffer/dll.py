class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None
        self.prev = None

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
        ct = 0
        if not self.isEmpty():
            item = self.start
            while (item != None and ((ct <= index) or (index == -1))):
                yield item
                item = item.nxt
                ct += 1

    def revTraverse(self, index: int = -1):
        """
        Traverses the list in reverse and returns the Node
        """
        ct = self.totalCount
        if not self.isEmpty():
            item = self.end
            while (item != None and ((ct > index))):
                yield item
                item = item.prev
                ct -= 1

    def append(self, data, index: int = -1):
        """
        Adds an item to the list. Default (-1) appends to end. -2 appends at start.
        """
        self.totalCount+=1
        if self.isEmpty():
            self.start = Node(data)
            self.start.prev = None
            self.seeks.append(self.start)
            self.end = self.start
        elif index == -2:    
            tmp = self.start
            self.start = Node(data)
            self.start.prev = None
            self.start.nxt = tmp
            
            newseeks = [self.start]
            for seek in self.seeks:
                if seek.prev != None:
                    newseeks.append(seek.prev)
            self.seeks = newseeks
        else:
            newNode = Node(data)
            
            lastitem = None
            for lastitem in self.Traverse(index): pass
            
            if lastitem != None:
                newNode.nxt = lastitem.nxt
            else:
                newNode.nxt = None
            newNode.prev = lastitem
            
            lastitem.nxt = newNode
            if newNode.nxt!=None:
                newNode.nxt.prev = newNode
            else:
                self.end = newNode

            ct = 0
            newseeks = []
            for seek in self.seeks:
                if ct > index:
                    if seek.prev != None:
                        newseeks.append(seek.prev)
                    else:
                        newseeks.append(seek)
                else: newseeks.append(seek)
                ct += self.seekintv
            self.seeks = newseeks
            if self.getNewRequiredSeek():
                self.seeks.append(self.end)
        
    
    def delete(self, index: int = -1):
        """
        Deletes item at index. Default (-1) deletes at end. -2 deletes at start.
        """
        self.totalCount -= 1
        if self.isEmpty():
            return
        elif index == -2:
            tmp = self.start
            self.start = self.start.nxt
            newseeks = []
            for seek in self.seeks:
                if seek.nxt != None:
                    newseeks.append(seek.nxt)
            self.seeks = newseeks
            del tmp
        else:
            lastitem = None
            for lastitem in self.Traverse(index):
                pass
            
            prevNode = lastitem.prev
            nextNode = lastitem.nxt
            prevNode.nxt = nextNode
            nextNode.prev = prevNode

            ct = 0
            newseeks = []
            for seek in self.seeks:
                if ct >= index:
                    if seek.nxt != None:
                        newseeks.append(seek.nxt)
                    else:
                        newseeks.append(seek)
                else: newseeks.append(seek)
                ct += self.seekintv
            self.seeks = newseeks
            if self.getDelRequiredSeek():
                self.seeks.remove(self.end)
            del lastitem

    def getPos(self, pos: int = -1):
        if pos == -1: return self.end
        if pos == 0: return self.start
        properMod = int((pos - (pos % self.seekintv)) / self.seekintv)
        modDiff = pos - self.seekintv * properMod
        x = self.seeks[properMod]
        if modDiff > 0:
            x = x.nxt
            modDiff-=1
        return x
    
    def getNewRequiredSeek(self):
        return ((self.totalCount - 1) % self.seekintv == 0) and (len(self.seeks) < (self.totalCount + 1) / self.seekintv)
    
    def getDelRequiredSeek(self):
        return ((self.totalCount - 1) % self.seekintv != 0) and (len(self.seeks) > (self.totalCount + 1) / self.seekintv)
    
    

    
        


x = DoublyLinkedList(2)
x.append("test")
x.append("test1")
x.append("test2")
"""
print("Initial Data")
print([y.data for y in x.Traverse()])
print("Initial Seeks")
for n in x.seeks:
    print(n.data)


x.append("wow", 1)
print("After Append")
print([y.data for y in x.Traverse()])
for n in x.seeks:
    print(n.data)

x.delete(2)
print("After Deletion")
print([y.data for y in x.Traverse()])
for n in x.seeks:
    print(n.data)
"""

print(x.getPos(0).data)