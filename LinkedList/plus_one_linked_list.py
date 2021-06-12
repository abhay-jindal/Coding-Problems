"""
    Add 1 to a number represented as linked list

    https://www.geeksforgeeks.org/add-1-number-represented-linked-list/

    Number is represented in linked list such that each digit corresponds to 
    a node in linked list. Add 1 to it. For example 1999 is represented as 
    (1-> 9-> 9 -> 9) and adding 1 to it should change it to (2->0->0->0) 

"""

from main import LinkedList

def plus_one_list(head):
    pass


if __name__ == "__main__":
    n = int(input('Enter the number of nodes: '))
    vals = list(map(int,input("\nEnter the node values for first list in space separated manner: ").strip().split()))[:n]
    list = LinkedList()
    list.insert_nodes(vals)
    print(f"Linkedlist: {list1}")  # to print linkedlist representation in 1 -> 2 -> 3 -> None



