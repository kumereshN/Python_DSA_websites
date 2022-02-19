from typing import List
from collections import deque


def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    queue = deque()
    num_row = len(dungeon_map)
    num_col  = len(dungeon_map[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    INF = 2147483647
    
    # Find all the coordinates for the entry, which is 0, to the queue
    for i, row in enumerate(dungeon_map):
        for j, entry in enumerate(row):
            if entry == 0:
                queue.append((i, j))
    while queue:
        row, col = queue.popleft()
        for delta_row, delta_col in directions:
            total_row, total_col = row + delta_row, col + delta_col
            if 0 <= total_row < num_row and 0 <= total_col < num_col:
                if dungeon_map[total_row][total_col] == INF:
                    # Takes the previous tile and adding 1 and replacing the number on the current tile.
                    dungeon_map[total_row][total_col] = dungeon_map[row][col] + 1
                    queue.append((total_row, total_col))
    return dungeon_map

dungeon_map = [[0,-1], [2147483647,2147483647]]
print(map_gate_distances(dungeon_map))