from typing import Any


class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self) -> None:
        self._score = float('-inf')
    

    def __call__(self, a: int) -> int:
        self._score = max(self._score, a) 
        return self._score
    

r = RecordScore()
print(r(10))
print(r(9))
print(r(11))