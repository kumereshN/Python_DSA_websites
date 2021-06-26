class TrainComposition:

    def __init__(self):
        self.wagons = dict()
        self.left  = 1
        self.right = 0

    def attach_wagon_from_left(self, wagonId):
        self.left -= 1
        self.wagons[self.left] = wagonId

    def attach_wagon_from_right(self, wagonId):
        self.right += 1
        self.wagons[self.right] = wagonId

    def detach_wagon_from_left(self):
        if self.left>self.right: return None
        wagonId = self.wagons[self.left]
        del self.wagons[self.left]
        self.left += 1
        return wagonId

    def detach_wagon_from_right(self):
        if self.left>self.right: return None
        wagonId = self.wagons[self.right]
        del self.wagons[self.right]
        self.right -= 1
        return wagonId


# Alternative, with deque
from collections import deque
class TrainComposition:

    def __init__(self):
        self.wagons = deque()

    def attach_wagon_from_left(self, wagonId):
        self.wagons.insert(0,wagonId)

    def attach_wagon_from_right(self, wagonId):
        self.wagons.append(wagonId)

    def detach_wagon_from_left(self):
        return self.wagons.popleft() if self.wagons else None

    def detach_wagon_from_right(self):
        return self.wagons.pop() if self.wagons else None
