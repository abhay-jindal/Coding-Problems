"""
    LinkedList class that will initialise an empty linkedlist with head as Null.
    Node class will actually create an node with next and val as attributes.

    Reference: https://realpython.com/linked-lists-python/

"""

class LinkedList:
    # constructor for creating an empty linkedlist with head as Null.
    def __init__(self):
        self.head = None

    # you can also add a __repr__ to classes to have a more helpful representation of the objects.
    def __repr__(self):
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    # get length of an list.
    def get_len(self):
        len, node = 0, self.head
        while node is not None:
            len += 1
            node = node.next
        return len

    # inserts single node in an linkedlist with given val.
    def insert_node(self, val):
        assert type(val) != list, 'given val should be of integer, float, boolean, char or string type only!'
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        return

    # inserts multiple nodes in an linkedlist with given vals as list of values.
    def insert_nodes(self, vals):
        assert type(vals) == list, 'given val should be of list type only!'

        start = 0
        if self.head is None:
            self.head = Node(vals[0])
            start = 1

        node = self.head
        while node.next is not None:
            node = node.next
        for i in range(start, len(vals)):
            node.next = Node(vals[i])
            node = node.next

class Node:
    # constructor for creating an list node with data as node's data & next pointer which points to next node in list.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # you can also add a __repr__ to classes to have a more helpful representation of the objects.
    def __repr__(self):
        return str(self.data)
    