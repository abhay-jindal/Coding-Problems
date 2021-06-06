"""
    Swap Nodes in Pairs

    https://leetcode.com/problems/swap-nodes-in-pairs/

    Given a linked list, swap every two adjacent nodes and return its head. 
    You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

"""

from main import LinkedList

def swap_pairs(head):

    # corner cases 
    if head is None or head.next is None:
        return head

    slow, fast = head, head.next # using two pointers approach, slow and fast pointer.
    new_head, rev_node = fast, None # store the first fast pointer which is the new head, rev_node to attach next pairs with current pair.
    while fast is not None:

        # break fast's next pointer, point fast next to previous node i.e. slow
        # point slow next to temp and repeat.
        temp = fast.next
        fast.next = slow
        slow.next = temp

        # for the first time no need to attach rev_node to any node. else attch it to fast pointer.
        if rev_node is not None:
            rev_node.next = fast

        # if fast's next is None or next's next is also none, then break.
        if temp is None or temp.next is None:
            break

        rev_node = slow
        slow = temp
        fast = temp.next    
    return new_head

def recursive_swap_pairs(head):
    if head is None or head.next is None:
        return head

    remaining = head.next.next
    new_head = head.next
    head.next.next = head
    head.next = recursive_swap_pairs(remaining)
    return new_head


if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"Original Linkedlist: {list}")  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    list.head = recursive_swap_pairs(list.head)
    print(f"Linkedlist after swapping pairs: {list}")


