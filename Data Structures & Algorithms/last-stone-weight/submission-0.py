import bisect

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones) > 1:
            x = stones.pop()
            y = stones.pop()
            if x != y:
                z = abs(x - y)
                bisect.insort(stones, z)
        
        if not stones:
            return 0
        else:
            return stones[0]