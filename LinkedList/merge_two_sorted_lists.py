"""
    Merge two sorted linked lists

    https://leetcode.com/problems/merge-two-sorted-lists/

    Given two sorted linked lists consisting of N and M nodes respectively. 
    The task is to merge both of the list (in-place) and return head of the merged list.
 
    valueN[] = {5,10,15,40}
    valueM[] = {2,3,20}
    Output: 2 3 5 10 15 20 40
    Explanation: After merging the two linkedlists, we have merged list as 2, 3, 5, 10, 15, 20, 40.

"""

from main import LinkedList, Node

def merge_two_lists(node1, node2):
    fake = Node(-1)
    node = fake
    while node1 is not None and node2 is not None:
        if node1.data >= node2.data:
            fake.next = node2 
            node2 = node2.next
        else:
            fake.next = node1
            node1 = node1.next
        fake = fake.next

    if node1 is not None:
        fake.next = node1
    else:
        fake.next = node2
    return node.next
 

if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted in first list: '))
    vals = list(map(int,input("\nEnter the node values for first list in space separated manner: ").strip().split()))[:n]
    list1 = LinkedList()
    list1.insert_nodes(vals)
    print(f"First Linkedlist: {list1}")  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    n1 = int(input('Number of nodes to be inserted in second list: '))
    vals = list(map(int,input("\nEnter the node values for second list in space separated manner: ").strip().split()))[:n1]
    list2 = LinkedList()
    list2.insert_nodes(vals)
    print(f"Second Linkedlist: {list1}")  # to print linkedlist representation in 1 -> 2 -> 3 -> None

    list1.head = merge_two_lists(list1.head, list2.head)
    print(f"Resultant list after merging two linkedlists: {list1}")


