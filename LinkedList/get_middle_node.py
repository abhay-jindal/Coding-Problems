"""
    Middle of the Linked List

    https://leetcode.com/problems/middle-of-the-linked-list/

    Given a non-empty, singly linked list with head node head, return a middle node of linked list.
    If there are two middle nodes, return the second middle node.

"""

from main import LinkedList

  
def get_middle_node(head):
    if head.next is None:
        return head

    slow, fast = head, head
    flag = False
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        # if fast is None:
            # flag = True
    # if flag:
        # print("LinkedList have even number of nodes.")
    # else:
        # print("LinkedList have odd number of nodes.")
    return slow



if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(list)  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    mid_node = get_middle_node(list.head)
    print(f"Middle node for given linkedlist: {mid_node.data}")
