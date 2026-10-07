class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = {0: 0, 1: 0}
        
        for i in range(2, len(cost)+1):
            min_1 = min_cost[i-1] + cost[i-1]
            min_2 = min_cost[i-2] + cost[i-2]
            min_cost[i] = min(min_1, min_2)
        
        return min_cost[len(cost)]


        