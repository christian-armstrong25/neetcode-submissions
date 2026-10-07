from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        available = Counter(nums)
        for i, n in enumerate(nums):
            if target - n in available:
                if target == 2*n and available[n] == 1:
                    continue
                return [i, nums.index(target - n, i+1)]

        