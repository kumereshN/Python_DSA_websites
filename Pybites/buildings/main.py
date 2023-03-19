from typing import List
from collections import defaultdict

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """
    lst_of_buildings = defaultdict(list)
    lst_of_buildings[WEST], lst_of_buildings[EAST]
    
    max_so_far = float('-inf')
    prev_height = -1
    
    
    for idx, cur_height in enumerate(buildings):
        if max_so_far < cur_height:
            max_so_far = cur_height
            lst_of_buildings[WEST].append(idx)
            lst_of_buildings[EAST] = [] # Reset the EAST side
        
        elif cur_height >= prev_height:
            lst_of_buildings[EAST].pop(-1)
        
        lst_of_buildings[EAST].append(idx)
        prev_height = cur_height
    return lst_of_buildings
            
    
A = [3, 5, 4, 4, 7, 1, 3, 2]
B = [1, 1, 1, 1, 1, 2]  # almost flat

search_apartment(A, WEST)