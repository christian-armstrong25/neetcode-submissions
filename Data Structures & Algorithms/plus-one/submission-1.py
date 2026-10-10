class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] == 10:
            if digits[:-1]:
                return self.plusOne(digits[:-1]) + [0]
            else:
                return [1, 0]
        return digits
        