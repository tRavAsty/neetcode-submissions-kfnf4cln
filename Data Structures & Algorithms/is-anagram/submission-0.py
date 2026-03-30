from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for c in s:
            cur = freq.get(c,0)
            freq[c] = cur+1
        
        for c in t:
            if c not in freq:
                return False
            else:
                freq[c]-=1
            
        for v in freq.values():
            if v!=0:
                return False
        return True




        