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
    if temp is None:
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

# delete node with given value in an binary search tree.
def deleteNode(node, value):
    if node is None:
        return None
    if node.data > value:
        node.left = deleteNode(node.left, value)
    elif node.data < value:
        node.right = deleteNode(node.right, value)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = smallestSuccessor(node.right)
        node.data = temp.data
        node.right = deleteNode(node.right, temp.data)
    return node

# helper function to find smallest left node of given node.
def smallestSuccessor(node):
    while node.left:
        node = node.left
    return node

# function to find the height of an given tree using recursion.
def heightTree(node):
    if node is None:
        return 0
    else:
        lHeight = heightTree(node.left)
        rHeight = heightTree(node.right)
        if lHeight > rHeight:
            return lHeight + 1
        else:
            return rHeight + 1

# print level order of an given binary tree.
def printLevelOrderBfs(node):
    height = heightTree(node)
    print(height)
    for i in range(height+1):
        printGivenLevel(node, i)

# helper function to actually print the given level node values.
def printGivenLevel(node, level):
    if node is None:
        return None
    elif level == 0:
        print(node.data, end=" ")
    else:
        printGivenLevel(node.left, level-1)
        printGivenLevel(node.right, level-1)


if __name__ == "__main__":
    n = int(input("Enter the root value: "))

    root = newNode(n)
    nodes = int(input("Enter the number of nodes: "))
    while nodes > 0:
        value = int(input("Enter the node value: "))
        root = insertElement(root, value)
        nodes -= 1

    inOrder(root)
    # deleteValue = int(input("Enter the node value to delete: "))
    # root = deleteNode(root, deleteValue)
    print('\n')
    printLevelOrderBfs(root)




