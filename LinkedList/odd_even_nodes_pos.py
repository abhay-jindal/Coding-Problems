"""
    Rearrange a linked list such that all even and odd positioned nodes are together

    https://www.geeksforgeeks.org/rearrange-a-linked-list-such-that-all-even-and-odd-positioned-nodes-are-together/

    Rearrange a linked list in such a way that all odd position nodes are together and all even positions node are together.

    Input:   1->2->3->4
    Output:  1->3->2->4

    Input:   10->22->30->43->56->70
    Output:  10->30->56->22->43->70

"""

from main import LinkedList, Node

# function to segregate nodes by changing their links.
def segregate_nodes(head):
 
    # corner cases
    if head is None or head.next is None or head.next.next is None:
        return

    # make dummy node
    odd_fake = Node(-1)
    even_fake = Node(-1)

    # storing the head of above nodes.
    odd_head, even_head = odd_fake, even_fake
    curr, flag = head, True
    while curr is not None:
        if flag:
            even_fake.next = curr
            even_fake = even_fake.next
            flag = False
        else:
            odd_fake.next = curr
            odd_fake = odd_fake.next
            flag = True
        curr = curr.next

    # attach three nodes accordingly
    even_fake.next = odd_head.next 
    odd_fake.next = None
    return even_head.next


# interchanging changes using two pointers approach, fast and slow pointer.
def segregate_nodes_2(head):

    # corner cases, atleast there should be 3 nodes to further proceed.
    if head is None or head.next is None or head.next.next is None:
        return head

    odd = head  # slow pointer
    even = head.next  # fast pointer
    even_head = even  # head of fast pointer
    while even and even.next:
        odd.next = even.next
        odd = odd.next  
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head
 

if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]

    list = LinkedList()
    list.insert_nodes(vals)
    print(list)  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    new_head = segregate_nodes_2(list.head)
    list.head = new_head
    print(f"Linked list after even odd segregation: {list}")
 

   