"""
BINARY TREE DATA STRUCTURE

A tree whose elements have at most 2 children is called a binary tree.
The maximum number of nodes at level ‘l’ of a binary tree is 2**l.
Maximum number of nodes in a binary tree of height ‘h’ is 2h – 1.
"""


# A class that represents an individual node of an binary tree
class newNode():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# Insert new node in a binary tree
def insert(node, key):
    if not node:
       root = newNode(key)
       return

    treeNodes = [node]
    while treeNodes:
        temp = treeNodes.pop(0)
        if not temp.left:
            temp.left = newNode(key)
            break
        else:
            treeNodes.append(temp.left)
        if not temp.right:
            temp.right = newNode(key)
            break
        else:
            treeNodes.append(temp.right)

def heightTree(node):
    if node is None:
        return 1
    else:
        lHeight = heightTree(node.left)
        rHeight = heightTree(node.right)
        if lHeight > rHeight:
            return lHeight + 1
        else:
            return rHeight + 1


# Depth First Traversal: Inorder (Left, Root, Right)
def inOrder(temp):
    if not temp:
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


if __name__ == "__main__":

    n = int(input("Enter the root value: "))
    root = newNode(n)
    nodes = int(input("Enter the number of nodes: "))
    while nodes > 0:
        value = int(input("Enter the node value: "))
        insert(root, value)
        nodes -= 1

    inOrder(root)
    print("\n")
    preOrder(root)
    print("\n")
    postOrder(root)

