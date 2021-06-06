"""
    Segregate even and odd nodes in a Linked List

    https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

    Given a Linked List of integers, write a function to modify the linked list such that 
    all even numbers appear before all the odd numbers in the modified linked list. 
    Also, keep the order of even and odd numbers same.

    Input: 17->15->8->12->10->5->4->1->7->6->NULL
    Output: 8->12->10->4->6->17->15->5->1->7->NULL

"""

from main import LinkedList, Node

# function to segregate nodes by changing their links.
def segregate_nodes(head):
 
    # corner cases
    if head is None or head.next is None:
        return

    # make dummy node
    odd_fake = Node(-1)
    even_fake = Node(-1)

    # storing the head of above nodes.
    odd_head, even_head = odd_fake, even_fake
    curr = head
    while curr is not None:
        if (curr.data%2) == 0:
            even_fake.next = curr
            even_fake = even_fake.next
        else:
            odd_fake.next = curr
            odd_fake = odd_fake.next
        curr = curr.next

    # attach three nodes accordingly
    even_fake.next = odd_head.next 
    odd_fake.next = None
    return even_head.next
 

if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(list)  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    new_head = segregate_nodes(list.head)
    list.head = new_head
    print(f"Linked list after even odd segregation: {list}")
 

   