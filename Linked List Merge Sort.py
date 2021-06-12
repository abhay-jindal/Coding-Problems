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


# class to create a new node of an linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None




    


