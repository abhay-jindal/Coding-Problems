"""
     Remove Duplicates from Sorted List

    https://leetcode.com/problems/remove-duplicates-from-sorted-list/

    Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
    Return the linked list sorted as well.

"""

from main import LinkedList


def remove_duplicates(head):
    if head is None or head.next is None:
        return head

    curr = head
    while curr.next is not None:  
        if curr.next.data == curr.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def remove_duplicates_recursive(head):
    if head is None:
        return head

    head.next = remove_duplicates_recursive(head.next)
    if (head.next is not None) and (head.data == head.next.data):
        return head.next

    return head
        

if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"Sorted List including duplicates: {list}")

    remove_duplicates(list.head)
    print(f"Sorted List excluding duplicates: {list}")

   


