class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    
    def dfs(root, max_so_far):
        if not root:
            return 0
        
        total = 0
        if max_so_far <= root.val:
            total += 1
            max_so_far = root.val
        
        total += dfs(root.left, max_so_far)
        total += dfs(root.right, max_so_far)
        
        return total
    return dfs(root, float('-inf'))