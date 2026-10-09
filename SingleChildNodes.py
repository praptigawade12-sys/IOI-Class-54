class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def single_child(root):
    if root is None:
        return

    if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
        print(root.data, end=" ")

    single_child(root.left)
    single_child(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.right = Node(5)

single_child(root)