"""
    Sort a linked list of 0s, 1s and 2s by changing links

    https://www.geeksforgeeks.org/sort-linked-list-0s-1s-2s-changing-links/

    Given a linked list of 0s, 1s and 2s, sort it.

    Input  : 2->1->2->1->1->2->0->1->0
    Output : 0->0->1->1->1->1->2->2->2
    The sorted Array is 0, 0, 1, 1, 1, 1, 2, 2, 2.

"""

from main import LinkedList, Node

# function to segregate nodes by changing their links.
def segregate_nodes(head):
 
    # corner cases
    if head is None or head.next is None:
        return

    # make three dummy nodes to store the references of occurrences if 0, 1 and 2
    zero_fake = Node(-1)
    one_fake = Node(-1)
    two_fake = Node(-1)

    # storing the head of above three nodes.
    zero, one, two = zero_fake, one_fake, two_fake

    curr = head
    while curr is not None:
        if curr.data == 0:
            zero_fake.next = curr
            zero_fake = zero_fake.next
        elif curr.data == 1:
            one_fake.next = curr
            one_fake = one_fake.next
        else:
            two_fake.next = curr
            two_fake = two_fake.next
        curr = curr.next

    # attach three nodes accordingly
    zero_fake.next = one.next 
    two_fake.next = None
  
    # in case 1's are not present then attach 0's with 2's.
    if one.next is None:
        zero_fake.next = two.next
    else:
        one_fake.next = two.next
    return zero.next



if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(list)  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    new_head = segregate_nodes(list.head)
    list.head = new_head
    print(f"Linked list after segregation: {list}")
 

   