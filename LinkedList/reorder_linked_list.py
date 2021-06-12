"""
    Reorder Linked List

    https://leetcode.com/problems/reorder-list/
    
    You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

"""

from main import LinkedList, Node
from get_middle_node import get_middle_node
from reverse_linked_list import reverse_list


def reorder_list(head):
    if head is None or head.next is None or head.next.next is None:
        return head

    before_mid = head 
    mid_node = get_middle_node(head)  # get middle node of linkedlist from where the next half will be reversed for comparison.
    next_to_mid = mid_node.next  # store next to mid in temp variable

    # make first half of list independent of second half, both lists will be treated as separate lists.
    mid_node.next = None
    after_mid = reverse_list(next_to_mid)  # reverse second half list and store the list in variable
    fake = Node(-1)
    new_head = fake
    flag = True

    # here the main comparison happens, as soon as we find unequal data, we return False.
    while after_mid is not None:
        if flag:
            fake.next = before_mid
            before_mid = before_mid.next
            flag = False
        else:
            fake.next = after_mid
            after_mid = after_mid.next
            flag = True
        fake = fake.next
    fake.next = before_mid  # mid one or two nodes will be left, adding them separately here.
    return new_head.next  


if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"List before arranging nodes: {list}")

    list.head = reorder_list(list.head)
    print(f"List after arranging nodes: {list}")


   


