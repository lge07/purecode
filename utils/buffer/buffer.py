from linkedlist import Node, DoublyLinkedList

class Buffer:
    def __init__(self, name: str):
        self.name = name
        self.file = None
        self.buffer = DoublyLinkedList(2)
        
        self.cursorX = 0
        self.cursorY = 0
    
    def newLine(self, contents: str = ""):
        nl = DoublyLinkedList(2)
        for char in contents:
            nl.append(char)
        self.buffer.append(nl)

    def getLine(self, lineno: int):
        line = ""
        for char in self.buffer.getIndex(lineno).Traverse():
            line += char
        return line
    
    def getBuffer(self):
        ret = []
        for lineno in range(self.buffer.totalCount):
            ret.append(self.getLine(lineno))
        return ret
                 
    
    # Required methods:
    # Writing characters to where the cursor currently is.
    # What happens when enter key is pressed
    # What happens when backspace is pressed
    # What happens when Tab is pressed
    # Copy/Paste/Cut: what happens when handling segments
    # Getting a segment or entire buffer as a string
    

