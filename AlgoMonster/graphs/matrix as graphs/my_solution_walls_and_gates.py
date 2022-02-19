from typing import List
from collections import deque

def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    num_row, num_col = len(dungeon_map), len(dungeon_map[0])
    queue = deque()
    INF = 2147483647
    
    for i, row in enumerate(dungeon_map):
        for j, entry in enumerate(row):
            if entry == 0:
                queue.append((i,j))
    
    def get_neighbor(coord):
        row, col = coord
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]
        
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_row and 0 <= neighbor_col < num_col:
                yield neighbor_row, neighbor_col
    
    def bfs(queue):
        row, col = queue[0]
        
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbor(node):
                total_row, total_col = neighbor
                if dungeon_map[total_row][total_col] == INF:
                    dungeon_map[total_row][total_col] = dungeon_map[row][col] + 1
                    queue.append(neighbor)
        return dungeon_map
     
    
    bfs(queue)

dungeon_map = [[0,-1], [2147483647,2147483647]]
map_gate_distances(dungeon_map)