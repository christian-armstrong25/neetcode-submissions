class Solution:

    def isValid(self, s: str) -> bool:
        left = set(['(', '{', '['])
        right_to_left = {
        ')': '(', 
        '}': '{', 
        ']': '['
        }

        stk = []
        for c in s:
            if c in left:
                stk.append(c)
            elif c in right_to_left:
                if not stk:
                    return False
                elif stk.pop() != right_to_left[c]:
                    return False
            else:
                return False
        return len(stk) == 0
        