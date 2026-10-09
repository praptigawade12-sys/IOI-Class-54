class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def largestBst(root):
    ans = [0]
    def dfs(n):
        if not n:
            return float("inf"),float("-inf"),0

        a,b,c = dfs(n.left)
        d,e,f = dfs(n.right)

        if b < n.data < d:
            size = c + f + 1
            ans[0] = max(size,ans[0])
            return min(a,n.data),max(e,n.data),size

        return float("-inf"),float("inf"),0

    dfs(root)
    return ans[0]

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(1)
root.left.right = Node(8)
root.right.right = Node(7)

print('Largest BST Sub Tree:',largestBst(root))