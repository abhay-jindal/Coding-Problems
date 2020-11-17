"""
LINKEDLIST MERGE SORT

"""

# Class to create an Linked list with an Null head pointer
class LinkedList:
    def __init__(self):
        self.head = None

    # append new_node in the linkedlist with the given data
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    # sorting of linked list using merge sort in O(nlogn) time complexity
    def mergeSort(self, head):
        if head == None or head.next == None:
            return head

        middle = self.printMiddle(head)
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

    # print linkedlist data
    def printList(self, head):
        if head is None:
            print(" ")
        curr_node = head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(" ")

    # get middle of an linkedlist, middle in case of odd nodes else second element in middle.
    def printMiddle(self, head):  
        slow = head 
        fast = head 
        flag = False
        while (fast != None and fast.next != None): 
            slow = slow.next
            fast = fast.next.next 
            if fast is None:
                flag = True
        if flag:
            print("LinkedList have even number of nodes.")
        else:
            print("LinkedList have odd number of nodes.")
        return slow
   
    # iteratively reverse the given list by changing the links of given list.
    def reverseList(self, head):
        curr = head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    # insert new node at the beginning of given linked list
    def insertNode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # deletes a particular node while head of the LinkedList is unknown. Exception for the last node!
    def deleteNode(self, node):
        if node.next is None:
            node = None
            return
        node.data = node.next.data
        temp = node.next.next
        node.next = temp

# class to create a new node of an linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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



if __name__ == "__main__":
    nodes = int(input("Enter number of nodes for linkedlist: "))
    llist = LinkedList()
    while nodes > 0:
        data = int(input("Enter data for node: "))
        llist.append(data)
        nodes -= 1

    # data = int(input("Enter data for new Node: "))
    # llist.insertNode(data)

    nodes = int(input("Enter number of nodes for second linkedlist: "))
    llist1 = LinkedList()
    while nodes > 0:
        data = int(input("Enter data for node: "))
        llist1.append(data)
        nodes -= 1

    head = mergeLists(llist.head, llist1.head)
    while head:
        print(head.data, end= " ")
        head = head.next


    # newList = LinkedList()
    # newList.addLists(llist.head, llist1.head)
 
    # newList.head = newList.mergeSort(newList.head)

    


