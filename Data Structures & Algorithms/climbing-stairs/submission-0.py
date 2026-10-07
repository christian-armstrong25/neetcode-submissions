class Solution:
    def climbStairs(self, n: int) -> int:
        distinct_ways = {0: 0, 1: 1, 2: 2}
        
        for i in range(3, n+1):
            distinct_ways[i] = distinct_ways[i-1] + distinct_ways[i-2]

        return distinct_ways[n]

        