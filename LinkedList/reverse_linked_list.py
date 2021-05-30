"""
    Reverse Linked List

    https://leetcode.com/problems/reverse-linked-list/
    Given a linked list of N nodes. The task is to reverse this list.

"""

from main import LinkedList

"""
    Iterative Method 

    Initialize two pointers prev as NULL, curr as head.
    Iterate through the linked list. In loop, do following. 
    // Before changing next of current, store next node in temp.
    next = curr->next
    // Now change next of current. This is where actual reversing happens.
    curr->next = prev 
    // Move prev and curr one step forward 
    prev = curr 
    curr = next

    Time Complexity: O(n) 
    Space Complexity: O(1)
"""
def reverse_list(head):
    if head is None or head.next is None:
        return head

    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# recursively reverse linkedlist
def recursive_reverse_list(head):
    if head is None or head.next is None:
        return head

    rest = recursive_reverse_list(head.next)
    head.next.next = head
    head.next = None
    return rest

# reverse linkedlist using stack data structure
def reverse_using_stack(head):
    if head is None or head.next is None:
        return head

    curr, stack = head, []
    while curr is not None:
        stack.append(curr)
        curr = curr.next

    head = temp = stack.pop()
    while stack:
        node = stack.pop()
        temp.next = node
        temp = node
    temp.next = None
    return head


if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"Original Linkedlist: {list}")  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    new_head = reverse_list(list.head)
    # new_head = reverse_using_stack(list.head)
    # new_head = recursive_reverse_list(list.head)
    list.head = new_head  # allot new head to linkedlist's head
    print(f"Reverse Linkedlist: {list}")


