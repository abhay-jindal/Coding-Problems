"""
     Remove Duplicates from Sorted List II

    https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

    Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
    leaving only distinct numbers from the original list. Return the linked list sorted as well.

"""

from main import LinkedList, Node


def remove_duplicates(head):
    if head is None or head.next is None:
        return head

    sentinel = Node(-1, head)

    # predecessor = the last node, before the sublist of duplicates
    pred = sentinel

    while head:
        # if it's a beginning of duplicates sublist skip all duplicates
        if head.next and head.data == head.next.data:
            # move till the end of duplicates sublist
            while head.next and head.data == head.next.data:
                head = head.next
            # skip all duplicates
            pred.next = head.next
        else:
            # otherwise, move predecessor
            pred = pred.next
        head = head.next
    return sentinel.next
        

if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"Sorted List including duplicates: {list}")

    list.head = remove_duplicates(list.head)
    print(f"Sorted List excluding duplicates: {list}")

   


