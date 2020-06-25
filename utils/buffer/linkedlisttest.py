import unittest
from linkedlist import DoublyLinkedList, Node

class TestDLLMethods(unittest.TestCase):
    def setUp(self):
        self.ll = DoublyLinkedList(2)
    
    def getData(self) -> list:
        return [x.getData() for x in self.ll.Traverse()]
    
    def getSeeks(self) -> list:
        return [x.getData() for x in self.ll.seeks]

    def testGet(self):
        # Bit of a chicken-and-egg:
        # Relies on append functioning as intended, yet seeing that append
        # functions as intended requires the get parametres to work properly.
        self.ll.append("node1")
        self.ll.append("node2")
        self.ll.append("node3")
        self.assertEqual(self.getData(), ["node1", "node2", "node3"])
        self.assertEqual([x.data for x in self.ll.revTraverse()], ["node3", "node2", "node1"])
        self.assertEqual(self.ll.getIndex().data, "node3")
        self.assertEqual(self.ll.getIndex(1).data, "node2")
        

    def test_append(self):
        # Case 1: Append to an empty list with index supplied
        # Shows that isEmpty is functional, therefore no need to test other indicies.
        self.ll.append("node1", -1)
        self.assertEqual(self.getData(), ["node1"])
        self.assertEqual(self.getSeeks(), ["node1"])
        
        # Case 2: Append to the start of the list
        self.ll.append("node2", 0)
        self.assertEqual(self.getData(), ["node2", "node1"])
        self.assertEqual(self.getSeeks(), ["node2"])
        
        # Case 3: Append somewhere in between
        # Also tests if a new seek is added when conditions are satisfied.
        self.ll.append("node3", 1)
        self.assertEqual(self.getData(), ["node2", "node3", "node1"])
        self.assertEqual(self.getSeeks(), ["node2", "node1"])
        
        # Case 4: Append to the end
        # Also tests if the seek system handles the addition correctly.
        self.ll.append("node4", -1)
        self.assertEqual(self.getData(), ["node2", "node3", "node1", "node4"])
        self.assertEqual(self.getSeeks(), ["node2", "node1"])

        # Cases 5, 6: Appends to invalid indicies
        # Makes sure that nothing happens when an invalid index is passed.
        self.ll.append("node5", -2)
        self.assertEqual(self.getData(), ["node2", "node3", "node1", "node4"])
        self.assertEqual(self.getSeeks(), ["node2", "node1"])

        self.ll.append("node6", 100)
        self.assertEqual(self.getData(), ["node2", "node3", "node1", "node4"])
        self.assertEqual(self.getSeeks(), ["node2", "node1"])
    
    def test_delete(self):
        # Setup: creates the same list as in the prior test for convenience
        self.ll.append("node1", -1)
        self.ll.append("node2", 0)
        self.ll.append("node3", 1)
        self.ll.append("node4", -1)
        
        # Case 1, 2: Delete from invalid indicies
        # Makes sure that nothing happens when an invalid index is passed
        el = self.ll.delete(-2)
        self.assertEqual(self.getData(), ["node2", "node3", "node1", "node4"])
        self.assertEqual(self.getSeeks(), ["node2", "node1"])
        self.assertIsNone(el)

        el = self.ll.delete(100)
        self.assertEqual(self.getData(), ["node2", "node3", "node1", "node4"])
        self.assertEqual(self.getSeeks(), ["node2", "node1"])
        self.assertIsNone(el)

        # Case 3: Delete from end
        # Also tests if seek system handles the removal correctly.
        el = self.ll.delete(-1)
        self.assertEqual(self.getData(), ["node2", "node3", "node1"])
        self.assertEqual(self.getSeeks(), ["node2", "node1"])
        self.assertEqual(el.getData(), "node4")
        
        # Case 4: Delete from somewhere in between
        # Also tests if a seek is removed when conditions are satisfied
        el = self.ll.delete(1)
        self.assertEqual(self.getData(), ["node2", "node1"])
        self.assertEqual(self.getSeeks(), ["node2"])
        self.assertEqual(el.getData(),"node3")

        # Case 5: Delete from the start of the list.
        el = self.ll.delete(0)
        self.assertEqual(self.getData(), ["node1"])
        self.assertEqual(self.getSeeks(), ["node1"])
        self.assertEqual(el.getData(), "node2")
        
        # Case 6: Delete final element
        el = self.ll.delete(-1)
        self.assertEqual(self.getData(), [])
        self.assertEqual(self.getSeeks(), [])
        self.assertEqual(el.getData(), "node1")
        
if __name__ == "__main__":
    unittest.main()
