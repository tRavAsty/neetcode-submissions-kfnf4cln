from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #match_dict
        n = len(s)
        res = [False for _ in range(n+1)]
        res[0] = True

        for i in range(n):
            if not res[i]:
                continue
            for word in wordDict:
                l = len(word)
                if i+l<=n and s[i:i+l] == word:
                    res[i+l] = True
        
        return res[n]


        