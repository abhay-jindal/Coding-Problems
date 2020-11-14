"""
BINARY SEARCH TREE DATA STRUCTURE

A tree whose elements have at most 2 children is called a binary tree.
A tree whose parent' value is greater then its left child's value is BST.
Inorder traversal of BST is always sorted sequence of node values.
"""


# A class that represents an individual node of an binary tree
class newNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Depth First Traversal: Inorder (Left, Root, Right)
def inOrder(temp):
    if (not temp):
        return
    inOrder(temp.left)
    print(temp.data, end= " ")
    inOrder(temp.right)

# Depth First Traversal: Preorder (Root, Left, Right)
def preOrder(temp):
    if not temp.left:
        return
    print(temp.data, end= " ")
    preOrder(temp.left)
    inOrder(temp.right)

# Depth First Traversal: Postorder (Left, Right, Root)
def postOrder(temp):
    if not temp:
        return
    postOrder(temp.left)
    postOrder(temp.right)
    print(temp.data, end= " ")

# Search an element in binary Search tree using Binary Search Algorithm.
# Time complexity O(h) where h is height of tree.
def searchElement(node, value):
    if node is None:
        return False
    if node.data == value:
        return True
    elif node.data > value:
        return searchElement(node.left, value) # searches for left sub tree.
    else:
        return searchElement(node.right, value) # searches for right sub tree.

# Insert an element in binary Search tree recursively
# Worst case Time complexity O(h) where h is height of tree.
def insertElement(node, value):
    if node is None:
        return newNode(value)
    else:
        if node.data == value:
            return node
        elif node.data > value:
            node.left = insertElement(node.left, value)
        else:
            node.right = insertElement(node.right, value)
    return node


if __name__ == "__main__":
    n = int(input("Enter the root value: "))
    root = newNode(n)
    nodes = int(input("Enter the number of nodes: "))
    while nodes > 0:
        value = int(input("Enter the node value: "))
        root = insertElement(root, value)
        nodes -= 1

    inOrder(root)


