class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        
    def add(self, val: int) -> int:
        if not self.nums:
            self.nums = [val]
            return self.nums[-self.k]
        
        l, r = 0, len(self.nums) - 1
        while l < r:
            m = l + (r-l)//2
            if val <= self.nums[m]:
                r = m - 1
            elif val > self.nums[m]:
                l = m + 1
        
        if val <= self.nums[l]:
            self.nums = self.nums[:l] + [val] + self.nums[l:]
        else: 
            self.nums = self.nums[:l+1] + [val] + self.nums[l+1:]

        return self.nums[-self.k]