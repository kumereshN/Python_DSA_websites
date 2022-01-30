from collections import deque
from typing import List

def count_number_of_islands(grid: List[List[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])

    def get_neighbors(coord):
        res = []
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                res.append((neighbor_row, neighbor_col))
        return res

    def bfs(start):
        queue = deque([start])
        r, c = start
        grid[r][c] = 0
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node):
                r, c = neighbor
                if grid[r][c] == 0:
                    continue
                queue.append(neighbor)
                # Fill the visited nodes with 0
                grid[r][c] = 0

    count = 0
    # bfs starting from each unvisited land cell
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                continue
            bfs((r, c))
            count += 1 # bfs would find 1 connected island, increment count
    return count