def lca(root, node1, node2):
    if not root:
        return

    if node1.val < root.val and node2.val < root.val:
        return lca(root.left, node1, node2)
    if node1.val > root.val and node2.val > root.val:
        return lca(root.right, node1, node2)
    
    return root