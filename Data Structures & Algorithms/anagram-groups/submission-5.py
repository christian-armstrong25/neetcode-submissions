from collections import Counter 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        ans = []
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in map:
                ans[map[ss]].append(s)
            else:
                map[ss] = len(ans)
                ans.append([s])
        return ans

        
        
            



        