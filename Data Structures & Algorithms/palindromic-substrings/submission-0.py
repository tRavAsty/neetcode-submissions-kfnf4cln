class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            # central is the character
            l = i
            r = i
            while l>=0 and r <n and s[l] == s[r]:
                res+=1
                l-=1
                r+=1

            # central is the space next the character
            l = i
            r = i+1
            while l>=0 and r <n and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
        return res
        