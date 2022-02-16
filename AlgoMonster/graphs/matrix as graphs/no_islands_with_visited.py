from typing import List
from collections import deque

def count_number_of_islands(grid: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    num_row, num_col = len(grid), len(grid[0])
    
    def get_neighbor(coord):
        row, col = coord
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]
        
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_row and 0 <= neighbor_col < num_col:
                if grid[neighbor_row][neighbor_col] == 1:
                    yield neighbor_row, neighbor_col
                
    def bfs(root):
        row, col = root
        queue = deque([root])
        visited = [[False for _ in range(num_col)] for _ in range(num_row)]
        visited[row][col] = True
        
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbor(node):
                row, col = neighbor
                if visited[row][col] == True:
                    continue
                visited[row][col] = True
                queue.append(neighbor)
    
    count = 0
    for row in range(num_row):
        for col in range(num_col):
            bfs((row,col))
            count += 1
            
    return count

grid = [[1,1,1,0,0,0],
[1,1,1,1,0,0],
[1,1,1,0,0,0],
[0,1,0,0,0,0],
[0,0,0,0,1,0],
[0,0,0,0,0,0]]

count_number_of_islands(grid)