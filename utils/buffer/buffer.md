# Buffer

## Why?

The buffer is a place for the lines of a document to be stored in an organised fashion. Python is probably so bloated that the performance difference over using a list of lists (the horror) isn't terribly significant, but it's still good practice to write an actual data structure to hold things.

The text buffer uses a doubly linked list as the base unit. Each line is meant to be a doubly-linked-list of characters, and each document is meant to be a doubly linked list of lines. While the memory penalty may be larger than a singly-linked list, it's easier to traverse and affords better performance.

The Wikipedia article on [doubly-linked lists](https://en.wikipedia.org/wiki/Doubly_linked_list) is a sufficient introductory article.

This implementation puts "seek" intervals throughout the linked list, to facilitate quicker access to certain parts of the list. The seek interval can be changed in structure init, and while it does use additional memory, they will probably be useful with larger documents - fewer iterations of traversing will probably be helpful in the long run.

It's otherwise a fairly standard doubly-linked-list implementation, perhaps with some off-loading of what would normally be in the list itself to the Node. 

## Required Code
- Node class
  - Data elements:
    - ``data (any)``: information stored within the node
    - ``prev (Node, None)``: previous item: ``Node`` in normal cases, ``None`` if start.
    - ``nxt (Node, None)``: next item: ``Node`` in normal cases, ``None`` if end.
  - Functions
    - ``isStart -> bool``: convenience function to check if current ``Node`` is at start (``prev == None``)
    - ``isEnd -> bool``: convenience function to check if current ``Node`` is at end (``nxt == None``)
    - ``addInRear(node: Node) -> None``: adds a ``Node`` in the position before the current ``Node``.
    - ``addInFront(node: Node) -> None``: adds a ``Node`` in the position after the current ``Node``.
    - ``remove -> Node``: removes and returns current ``Node``
## Notes on Various Implementation Details

- How seek system works
- How the most efficient access method works