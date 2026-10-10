import math

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])

        while n != 1:
            new_n = 0
            while n > 0:
                i = math.floor(math.log(n, 10))
                digit = n // 10**i
                n -= digit * 10**i
                new_n += digit**2
            if new_n in seen:
                return False
            seen.add(new_n)
            n = new_n
        return True

        

        