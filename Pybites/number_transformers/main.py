from collections import deque


def num_ops(n):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """
    # keep a running history of where we've been and where we're going next
    visited = set()
    history = deque([(1, 0)])

    while history:

        track, ops_num = history.popleft()
        if track == n:
            break

        ops_num += 1
        if (track * 2) not in visited:
            new_track = track * 2
            visited.add(new_track)
            history.append((new_track, ops_num))

        if (track // 3) not in visited:
            new_track = track // 3
            visited.add(new_track)
            history.append((new_track, ops_num))

    return ops_num


print(num_ops(12))