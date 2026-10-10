import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        start = 1
        while start < len(ans):
            for i in range(start, len(ans), 2*start):
                for j in range(min(start, len(ans)-i)):
                    ans[i+j] += 1
            start *= 2
        return ans

        # 0, 1 // 1,    3,    5,    7,    9,     11
        # 0, 1 //    2, 3,       6, 7,       10, 11
        # 0, 1 //          4, 5, 6, 7,   

        