from collections import deque
from typing import List

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    """ r,c is the row and column tells you where the number has to be replaced """
    num_rows, num_cols = len(image), len(image[0])
    def get_neighbors(coord, color):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            # the neighboring row and column indexes surrounding the current rows and columns
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                # Find all the neighboring rows and cols that have the same color
                if image[neighbor_row][neighbor_col] == color:
                    yield neighbor_row, neighbor_col

    def bfs(root):
        queue = deque([root])
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        r, c = root
        color = image[r][c]
        # We've visited the first one, so replace the color
        image[r][c] = replacement # replace root color
        visited[r][c] = True
        while len(queue) > 0:
            node = queue.popleft()
            # Output each neighbor_row and neighbor_col one by one instead of the entire thing because of yield
            for neighbor in get_neighbors(node, color):
                r, c = neighbor
                if visited[r][c]:
                    continue
                # The color is found and replaced
                image[r][c] = replacement # replace color
                # Append the nighbors which have not been visited
                queue.append(neighbor)
                visited[r][c] = True

    bfs((r, c))
    return image