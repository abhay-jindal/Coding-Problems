"""
    Clockwise rotation of Linked List

    https://leetcode.com/problems/rotate-list/
    https://www.geeksforgeeks.org/clockwise-rotation-of-linked-list/

    Given a singly linked list and an integer K, the task is to rotate the linked list clockwise to the right by K places.

"""

from main import LinkedList

  
def rotate_list(head, k):
    if head is None or head.next is None:
        return head
 
    len, last_node = 1, head
    while last_node.next is not None:
        last_node = last_node.next
        len += 1

    # If k is greater than the size of the linked list
    if (k > len): k = k % len

    k = len - k  # Subtract from length to convert it into left rotation
    if (k == 0 or k == len):
        return head

    k_node, cnt = head, 1
    while cnt < k and k_node is not None:
        k_node = k_node.next
        cnt += 1

    last_node.next = head  # Change next of last node to previous head
    head = k_node.next      # Change head to (k+1)th node
    k_node.next = None   # Change next of kth node to None
    return head   # Return the updated head pointer


if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]
    k = int(input('Number of rotations: '))

    list = LinkedList()
    list.insert_nodes(vals)
    print(list)  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    new_head = rotate_list(list.head, k)
    while new_head is not None:
        print(new_head, end=" -> ")
        new_head = new_head.next

   