from collections import deque


def level_order_traversal(root):
    # WRITE YOUR BRILLIANT CODE HERE
    queue = deque([root])
    res = []

    # As long as there's an element in the queue
    while len(queue) > 0:
        new_level = []
        n = len(queue)
        # Number of nodes in the queue
        # Iterate the queue
        for _ in range(n):
            # Get the current node
            # Always starts from left, FIFO (First in First out)
            node = queue.pop()
            new_level.append(node.val)
            # Checks for the current node's children and appends them in queue
            for child in [node.right, node.left]:
                if child:
                    queue.append(child)
        res.append(new_level)
    return res
