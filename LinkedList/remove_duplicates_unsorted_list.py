"""
     Remove Duplicates from UnSorted List

    https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/

    Write a removeDuplicates() function that takes a list and deletes any duplicate nodes from the list. The list is not sorted. 
    For example if the linked list is 12->11->12->21->41->43->21 then removeDuplicates() should convert the list to 12->11->21->41->43. 

"""

from main import LinkedList


def remove_duplicates(head):
    if head is None or head.next is None:
        return head

    hash = set()
    hash.add(head.data)
    while head.next is not None:  
        if head.next.data in hash:
            head.next = head.next.next
        else:
            hash.add(head.next.data)
            head = head.next
       

if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"Sorted List including duplicates: {list}")

    remove_duplicates(list.head)
    print(f"Sorted List excluding duplicates: {list}")

   


