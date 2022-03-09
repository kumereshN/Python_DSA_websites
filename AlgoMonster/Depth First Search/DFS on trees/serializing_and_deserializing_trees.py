class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # WRITE YOUR BRILLIANT CODE HERE
    res = []
    def dfs(root):
        if not root:
            res.append('x')
            return
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return ' '.join(res)

def deserialize(s):
    # AND HERE
    def dfs(nodes):
        val = next(nodes)
        if val == 'x':
            return 0
        cur = Node(int(val))
        cur.left = dfs(nodes)
        cur.right = dfs(nodes)
        return cur
    
    return dfs(iter(s.split()))