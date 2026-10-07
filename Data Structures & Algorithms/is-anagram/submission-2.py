class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for l in s:
            m[l] = m.get(l, 0) + 1
    
        n = {}
        for l in t:
            n[l] = n.get(l, 0) + 1
        
        return m == n
        

