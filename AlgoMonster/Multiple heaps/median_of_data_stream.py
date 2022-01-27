from heapq import heappush, heappop

class MedianOfStream: 

    def __init__(self): 
        self.larger_half=[] #min_heap 
        self.smaller_half=[]#max_heap 

    def add_number(self, num: float) -> None: 
        # WRITE YOUR BRILLIANT CODE HERE
        heappush(self.larger_half, num)
        # smaller_half gets filled first
        if len(self.larger_half) > len(self.smaller_half):
            heappush(self.smaller_half, -1*heappop(self.larger_half))

    def get_median(self) -> float:
        # ALSO HERE
        # Length of the combined halfs is an even number, so (larger_half - (-smaller_half)) / 2
        if len(self.larger_half) == len(self.smaller_half):
            return (self.larger_half[0]-self.smaller_half[0])/2
        else:
            # Length of the combined halfs is an odd number, so get the largest number from the smaller half
            return -1*self.smaller_half[0]