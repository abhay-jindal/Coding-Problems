"""
    Reverse Nodes in k-Group

    https://leetcode.com/problems/reverse-nodes-in-k-group/
    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

    k is a positive integer and is less than or equal to the length of the linked list. 
    If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.

"""

from main import LinkedList
from reverse_linked_list import reverse_list


def reverse_k_group(head, k):
    if not head or not head.next:
            return head

    node, reverseNode = head, head
    for _ in range(k-1):
        node = node.next
    if node:
        temp = node.next
        node.next = None
        reverseNode = reverse_list(head)
        head.next = reverse_k_group(temp, k)
    return reverseNode
           


if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]
    k = int(input("Number of rotations: "))

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"Original Linkedlist: {list}")  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    list.head = reverse_k_group(list.head, k)
    print(f"{Linkedlist after k group rotations: {list}")


