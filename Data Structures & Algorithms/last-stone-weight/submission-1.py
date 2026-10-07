class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if x != y:
                stones.append(abs(x - y))
        
        if not stones: return 0
        else: return stones[0]