"""
    Partition a Linked List around a given value

    https://leetcode.com/problems/partition-list/
    
    Given the head of a linked list and a value x, partition it such that all nodes less 
    than x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the two partitions.

    Input:
        1->4->3->2->5->2->3, x = 3
    Output:
        1->2->2->3->3->4->5
    Explanation: 
        Nodes with value less than 3 come first, 
        then equal to 3 and then greater than 3.

"""

from main import LinkedList, Node

def partition_list(head, x):
    if head is None or head.next is None:
        return head

    fake1 = Node(-1)
    fake2 = Node(-1)
    new_head = fake1
    second_head = fake2
    while head is not None:
        if head.data < x:
            fake1.next = head
            fake1 = fake1.next
        else:
            fake2.next = head
            fake2 = fake2.next
        head = head.next
    fake2.next = None
    fake1.next = second_head.next
    return new_head.next


if __name__ == "__main__":
    n = int(input('Number of nodes to be inserted: '))
    vals = list(map(int,input("\nEnter the node values in space separated manner: ").strip().split()))[:n]
    x = int(input('Enter the partition value: '))

    list = LinkedList()
    list.insert_nodes(vals)
    print(f"List before partition of nodes around value {x}: {list}")

    list.head = partition_list(list.head, x)
    print(f"List after partition of nodes around value {x}: {list}")


   


