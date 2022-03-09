class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_height(tree: Node) -> int:
    if not tree:
        return 0
    
    left_tree_height = tree_height(tree.left)
    right_tree_height = tree_height(tree.right)
    
    if abs(left_tree_height - right_tree_height) > 1:
        return -1
        
    return max(left_tree_height, right_tree_height) + 1
        
def is_balanced(tree: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    return tree_height(tree) != -1