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
def insert(temp, key):
    if not temp:
        root = newNode(key)
        return

    q = []
    q.append(temp)
    while len(q):
        obj = q.pop(0)
        if not obj.left:
            obj.left = newNode(key)
            break
        else:
            q.append(obj.left)
        if not obj.right:
            obj.right = newNode(key)
            break
        else:
            q.append(obj.right)


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


if __name__ == "__main__":

    n = int(input("Enter the root value: "))
    root = newNode(n)

    root.left = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right = newNode(6)
    root.right.right = newNode(7)
    insert(root, 8)
    insert(root, 9)
    inOrder(root)
    print("\n")
    preOrder(root)
    print("\n")
    postOrder(root)

