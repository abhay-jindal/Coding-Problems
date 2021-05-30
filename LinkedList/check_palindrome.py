"""
    Palindrome Linked List

    https://leetcode.com/problems/palindrome-linked-list/
    https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/

    Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.

"""

from main import LinkedList
from get_middle_node import get_middle_node
from reverse_linked_list import reverse_list


def is_palindrome(head):
    if head is None or head.next is None:
        return True

    before_mid = head 
    mid_node = get_middle_node(head)  # get middle node of linkedlist from where the next half will be reversed for comparison.
    next_to_mid = mid_node.next  # store next to mid in temp variable

    # make first half of list independent of second half, both lists will be treated as separate lists.
    mid_node.next = None
    after_mid = reverse_list(next_to_mid)  # reverse second half list and store the list in variable

    # here the main comparison happens, as soon as we find unequal data, we return False.
    while after_mid is not None:
        if after_mid.data != before_mid.data:
            return False
        after_mid = after_mid.next
        before_mid = before_mid.next

    # if list is odd, then one node will be left after above comparisons, and we simply return True 
    if before_mid.next is None:
        return True

    # if list is even, two nodes will be left to compare, compare before_mid and its next and return accordingly.
    elif before_mid.data == before_mid.next.data:
        return True
    return False

# A simple solution is to use a stack of list nodes.
def is_palindrome_using_stack(head):
    if head is None or head.next is None:
        return True

    stack, curr = [], head
    while curr is not None:
        stack.append(curr.data)
        curr = curr.next

    curr = head
    nodes_to_check = len(stack)//2  # to check first half stack elements with first half of linkedlist
    while nodes_to_check != 0 and stack and curr is not None:
        temp = stack.pop()
        if curr.data != temp:
            return False
        curr = curr.next
        nodes_to_check -= 1
    return True


if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"Is list a Palindrome: {is_palindrome_using_stack(list.head)}")

   


