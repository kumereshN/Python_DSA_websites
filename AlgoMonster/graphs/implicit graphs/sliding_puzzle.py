from typing import List

def num_steps(init_pos: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    """
    For the moves variable:
    The way I understand it is:
    The key represents an index, it's value represent the indices it can be swapped with (the indices adjacent to it in the matrix)
    """
    moves = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}
    used, cnt = set(), 0
    s = "".join(str(c) for row in init_pos for c in row)
    # ('413205', 4) 
    # 4 is the index of "0"
    # start from 0 as it's the empty space in which you can move
    queue = [(s, s.index("0"))]
    while queue:
        # If the string has not been seen before in used, append the string to new
        # This will later be used for the new queue
        new = []
        for num, idx in queue:
            used.add(num)
            if num == "123450":
                return cnt
            arr = [c for c in num]
            for move in moves[idx]:
                # Making a copy of the array to avoid mutation
                new_arr = arr[:]
                # Possible outcomes from swapping "0" between the adjacent indexes
                new_arr[idx], new_arr[move] = new_arr[move], new_arr[idx]
                new_s = "".join(new_arr)
                if new_s not in used:
                    new.append((new_s, move))
        cnt += 1
        queue = new
    return -1

grid = [[4,1,3],
        [2,0,5]]

print(num_steps(grid))

"""
Source: https://leetcode.com/problems/sliding-puzzle/discuss/142758/Python-very-easy-to-understand-BFS-w-backtracking-concise-solution-beats-98
"""