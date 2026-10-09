class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kLargest = sorted(nums, reverse=True)[:k]
        print(self.kLargest)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.kLargest) < self.k:
            self.kLargest.append(val)
            self.kLargest.sort(reverse=True)
        elif self.kLargest[-1] < val:
            self.kLargest[-1] = val
            self.kLargest.sort(reverse=True)
        
        return self.kLargest[-1]



        
