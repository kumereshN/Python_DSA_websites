from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def ternary_tree_paths(root: Node) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    # dfs helper function
    def dfs(root, path, res):
        # exit condition, reached leaf node, append paths to results
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + str(root.val))
            return

        # dfs on each non-null child
        for child in root.children:
            if child:
                # The path is the state
                path.append(str(root.val))
                dfs(child, path, res)
                # Removes the last element in the path list to keep the first node and continue the dfs (Backtracking)
                path.pop()

    res = []
    if root:
        dfs(root, [], res)
    return res


def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
