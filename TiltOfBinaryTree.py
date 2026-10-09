class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def traverse(root,tilt):

    if root is None:
        return 0

    left = traverse(root.left,tilt)
    right = traverse(root.right,tilt)

    tilt[0] += abs(left-right)

    return left+right+root.data

def tilt(root):
    tilt=[0]
    traverse(root,tilt)
    return tilt[0]

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)

print("Tilt of Binary Tree is",tilt(root))