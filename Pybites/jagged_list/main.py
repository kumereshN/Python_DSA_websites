from typing import List
from itertools import zip_longest


def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:
    zipped_lst = zip_longest(*lst_of_lst, fillvalue = fillvalue)
    return [[item] for item in zip(*zipped_lst)]


lst, fill_value = [[1, 1, 1, 1],
                               [0, 0, 0, 0],
                               [1]], 1

print(jagged_list(lst, fill_value))