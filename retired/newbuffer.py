# A new buffer, utilising a linked list for further efficiency.
# TODO: Consider reimplemeting into an unrolled linked list or binary search tree.
from enum import Enum

class ChangeType(Enum):
    DELETE = -1
    ADD = 0
    APPEND = 1  # TODO: Think about whether append is necessary.
    

class Node:
    def __init__(self, to: Node, fr: Node, content: str):
        self.to = to
        self.fr = fr
        self.content = content
    
class DLinkedList:
    def __init__(self):
        self.start = None
    
    def appendNode(self, data: str):
        if self.start:
            # If self.start is not None
            pass
        if not self.start:
            # If self.start is None
            self.start = Node(None,None,data)

    def fTraverse(self):
        """
        Traverses the list forwards and returns node classes
        """
        node = self.start
        while node.to != None:
            yield node
        del node
    
    def rTraverse(self):
        """
        Traverses the list backwards and returns node classes
        """
        node = self.end
        while node.fr != None:
            yield node
        del node

    