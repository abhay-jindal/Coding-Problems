class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def createNode(parent, i, child, root):
    if child[i] is not None:
        return
    child[i] = Node(i)
    if parent[i] == -1:
        root[0] = child[i]
        return
    if child[parent[i]] is None:
        createNode(parent, parent[i], child, root)
    
    p = child[parent[i]]
    if p.left is None:
        p.left = child[i]
    else:
        p.right = child[i]
def createTree(parent, n):
    child = [None for i in range(n+1)]
    root = [None]
    for i in range(n):
        createNode(parent, i, child, root)
    return root[0]

def inOrder(node):
    if not node:
        return
    inOrder(node.left)
    print(node.key, end= " ")
    inOrder(node.right)

if __name__ == "__main__":
    n = int(input('Number of elements: '))
    parent = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
    root = createTree(parent, n)
    inOrder(root)