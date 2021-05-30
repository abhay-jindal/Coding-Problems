"""
    Clockwise rotation of Linked List

    https://leetcode.com/problems/rotate-list/
    https://www.geeksforgeeks.org/clockwise-rotation-of-linked-list/

    Given a singly linked list and an integer K, the task is to rotate the linked list clockwise to the right by K places.

"""

from main import LinkedList

 # function to return nth node from end of the list 
def get_nth_from_last(head, n):
    # corner cases
    if head is None or head.next is None:
        return head

    # get to the nth node of list
    start = head
    for _ in range(n-1):
        start = start.next

    # if n is out of range then start will be None, therefore return
    if start is None:
        return "Nth index out of range!"

    # initialize second pointer to again start from head while start pointer which is at nth index reaches the end 
    # of list.
    second_start = head
    while start.next is not None:
        start = start.next
        second_start = second_start.next

    return second_start


if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]
    k = int(input('Nth node position from end: '))

    list = LinkedList()
    list.insert_nodes(vals)
    print(list)  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    nth_node = get_nth_from_last(list.head, k)
    print(f"Node from end of linked list: {nth_node}")

   