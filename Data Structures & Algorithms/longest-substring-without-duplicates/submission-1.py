class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        l,r = 0,0
        n = len(s)
        res = 0
        while r<n:
            curr = s[r]
            if curr in pos and pos[curr] >= l:
                l = pos[curr]+1
            pos[curr] = r
            res = max(res,r-l+1)
            r+=1
        return res

        