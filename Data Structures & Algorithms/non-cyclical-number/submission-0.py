class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            seen.add(n)
            n = self.sumOfSquaredDigits(n)
            if n in seen:
                return False
        return True

    def sumOfSquaredDigits(self, n: int) -> int:
        ans = 0
        i = 0
        while n // 10**i > 0:
            last_i_digits = n % 10**(i+1)
            ith_digit = last_i_digits // 10**i
            ans += ith_digit**2
            n -= last_i_digits
            i += 1
        return ans