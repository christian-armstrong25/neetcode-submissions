class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        return [c[0] for c in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]
