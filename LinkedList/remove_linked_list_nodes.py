"""
    Remove Linked List Elements

    https://leetcode.com/problems/remove-linked-list-elements/

    Given the head of a linked list and an integer val, remove all the 
    nodes of the linked list that has Node.val == val, and return the new head.

"""

from main import LinkedList, Node


def remove_nodes(head, val):
    if head is None:
        return head

    sentinel = Node(-1, head)
    prev = sentinel
    curr = sentinel.next
    while curr is not None:  
        if curr.data == val:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    return sentinel.next
        

if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]
    val = int(input('Enter the node value to remove from list: '))

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"List including nodes with val {val}: {list}")

    list.head = remove_nodes(list.head, val)
    print(f"List excluding nodes with val {val}: {list}")

   


