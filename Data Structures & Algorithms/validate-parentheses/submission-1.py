class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        opening = {'(', '{', '['}
        closing = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for c in s:
            if c in opening:
                stk.append(c)
            elif stk and c == closing[stk[-1]]:
                stk.pop()
            else:
                return False
        return not stk
        