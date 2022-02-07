from typing import List
from collections import deque

def num_steps(combo: str, trapped_combos: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    depth = -1
    visited, q = set(trapped_combos), deque(['0000'])

    def successors(src):
        res = []
        for i, ch in enumerate(src):
            num = int(ch)
            # src[:i] is the pointer on the source
            # str((num - 1) % 10) changes the number where the pointer is currently pointing (This is the backwards combo)
            # str((num + 1) % 10) is the forward combo
            # src[i+1:] are the digits after the pointer
            res.append(src[:i] + str((num - 1) % 10) + src[i+1:])
            res.append(src[:i] + str((num + 1) % 10) + src[i+1:])
        return res

    while q:
        size = len(q)
        depth += 1
        for _ in range(size):
            node = q.popleft()
            if node == combo:
                return depth
            if node in visited:
                continue
            visited.add(node)
            q.extend(successors(node))
    return -1


combo = "0202"
trapped_combos = ["0201","0101","0102","1212","2002"]
print(num_steps(combo, trapped_combos))