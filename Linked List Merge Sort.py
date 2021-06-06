"""
LINKEDLIST MERGE SORT

"""

# Class to create an Linked list with an Null head pointer
class LinkedList:
    def __init__(self):
        self.head = None

    
    # sorting of linked list using merge sort in O(nlogn) time complexity
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.getMiddleNode(head)
        nextToMiddle = middle.next
        middle.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(nextToMiddle)
        sortedList = self.sortedMerge(left, right)
        return sortedList

    # helper function for merge sort to compare two elements of partitioned linkedlist.
    def sortedMerge(self, left, right):
        sortedList = None
        if left == None:
            return right
        if right == None:
            return left

        if left.data <= right.data:
            sortedList = left
            sortedList.next = self.sortedMerge(left.next, right)
        else:
            sortedList = right
            sortedList.next = self.sortedMerge(left, right.next)
        return sortedList

    # add two linkedlist nodes to create a new linkedlist with the sum of their values.
    def addLists(self, first, second):
        temp = None
        prev = None
        carry = 0
        while first is not None or second is not None:
            fData = 0 if first == None else first.data
            sData = 0 if second == None else second.data
            Sum = carry + fData + sData
            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10

            temp = Node(Sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        if carry > 0:
            temp.next = Node(carry)


# class to create a new node of an linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# function to merge two sorted lists in place using constant space.
def mergeLists(node, node1):
    fake = Node(-1)
    last = fake
  
    while node is not None and node1 is not None:
        if node.data <= node1.data:
            last.next = node
            last = node
            node = node.next
        else:
            last.next = node1
            last = node1
            node1 = node1.next
    if node is None:
        last.next = node1
    if node1 is None:
        last.next = node
    return fake.next



# reorder linkedlist in a1, an-1, a2, an-2.... format using O(1) auxillary space.
def reorderList(node):
    if node is None or node.next is None:
        return node

    middle = llist.getMiddleNode(node)
    curr = middle.next
    middle.next = None
    prev = llist.reverseList(curr)
    fake = Node(-1)
    last = fake
    flag = True
    while node is not None and prev is not None:
        if flag:
            last.next = node
            last = node
            node = node.next
            flag = False
        else:
            last.next = prev
            last = prev
            prev = prev.next
            flag = True
    if node is None:
        last.next = prev
    if prev is None:
        last.next = node
    return fake.next


    


