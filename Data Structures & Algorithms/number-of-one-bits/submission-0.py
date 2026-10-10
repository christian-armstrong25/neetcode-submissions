class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([1 for b in bin(n) if b == "1"])