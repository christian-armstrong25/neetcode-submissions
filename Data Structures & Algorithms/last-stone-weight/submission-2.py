import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                new_stone = abs(y - x)
                heapq.heappush(stones, -new_stone)
        return -stones[0] if stones else 0
                
                



        