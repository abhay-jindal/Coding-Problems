"""
    Clockwise rotation of Linked List

    https://leetcode.com/problems/rotate-list/
    https://www.geeksforgeeks.org/clockwise-rotation-of-linked-list/

    Given a singly linked list and an integer K, the task is to rotate the linked list clockwise to the right by K places.

"""

from main import LinkedList

 # function to return nth node from end of the list, passing the list to change its head for few test cases.
def get_nth_from_last(list, n):
    head = list.head

    # corner cases
    if head is None or head.next is None:
        return

    # get to the nth node of list from head.
    start = head
    temp = None
    for _ in range(n-1):
        start = start.next

    # if n is out of range then start will be None, therefore return
    if start is None:
        return 

    # initialize second pointer to again start from head while start pointer which is at nth index reaches the end 
    # of list.
    second_start = head
    before_nth_node = None
    while start.next is not None:
        before_nth_node = second_start  # to store (n+1)th node from end
        start = start.next
        second_start = second_start.next

    # if nth node from end is head itself, change head of the list to (n-1)th node
    if second_start is head:
        list.head = second_start.next
        return
    before_nth_node.next = second_start.next
    second_start.next = None


if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]
    k = int(input('Nth node position from end: '))

    list = LinkedList()
    list.insert_nodes(vals)
    print(list)  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    get_nth_from_last(list, k)
    print(f"List after removing nth node: {list}")

   