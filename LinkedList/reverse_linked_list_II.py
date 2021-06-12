"""
    Reverse Linked List II

    https://leetcode.com/problems/reverse-linked-list-ii/

    Given the head of a singly linked list and two integers left and right 
    where left <= right, reverse the nodes of the list from position left to 
    position right, and return the reversed list.

"""

from main import LinkedList, Node
from reverse_linked_list import reverse_list

"""
    Idea is to make three separate lists, predecessor list upto left pos.
    Reversed list from left pos to right pos.
    Successor list from right pos to original list's tail.
    Connect predecessor->reverse_between_list->successor.
"""
def reverse_between(head, left, right):
    if head is None or head.next is None or right == 1:
        return head

    #sentinel node handling positions starting from 1
    sentinel = Node(-1, head)
    # left predecessor of left position node. Helpful to link the reversed part head.
    left_pred = sentinel

    # update left predecessor upto the left position
    while left_pred is not None and left > 1:
        left_pred = left_pred.next
        left -= 1
        # decrement right pos as well to avoid starting from head again 
        right -= 1 

    # right_pred = left position node, new head for the list to be reversed.
    right_pred = left_pred.next
    # save reference of right predecessor as it will act as tail of the reversed list
    reverse_tail = right_pred
    # left predecessor next will be None.
    left_pred.next = None

    # update right predecessor upto the right position
    while right_pred is not None and right > 1:
        right_pred = right_pred.next
        right -= 1

    # successor of right position.
    right_successor = right_pred.next
    right_pred.next = None

    reverse_head = reverse_list(reverse_tail) # reversing the left to right pos list.
    # below two steps: predecessor->reverse_between_list->successor
    left_pred.next = reverse_head
    reverse_tail.next = right_successor

    return sentinel.next


if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]
    left = int(input('Left position to reverse list from: '))
    right = int(input('Right position to reverse list to: '))

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"Original Linkedlist: {list}")  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    list.head = reverse_between(list.head, left, right)
    print(f"Reverse Linkedlist: {list}")


