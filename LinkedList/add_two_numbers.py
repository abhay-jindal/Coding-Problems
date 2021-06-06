"""
    Add Two Numbers

    https://leetcode.com/problems/add-two-numbers/

    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

"""

from main import LinkedList, Node

def add_two_numbers(node1, node2):
    fake = Node(-1)
    node = fake
    carry = 0
    while node1 is not None or node2 is not None:
        val1 = node1.data if node1 is not None else 0
        val2 = node2.data if node2 is not None else 0
        sum = val1 + val2 + carry
        carry = 1 if sum > 9 else 0

        node.next = Node(sum%10)
        node = node.next
        if node1 is not None:
            node1 = node1.next

        if node2 is not None:
            node2 = node2.next
    if carry:
        node.next = Node(carry)
    return fake.next


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

    list1.head = add_two_numbers(list1.head, list2.head)
    print(f"Linkedlist after swapping pairs: {list1}")


