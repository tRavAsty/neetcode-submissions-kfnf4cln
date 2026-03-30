class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0:
            return res

        n = len(strs[0])
        for i in range(n):
            cur = strs[0][i]
            for s in strs[1:]:
                if i>=len(s) or cur!=s[i]:
                    return res
            res+=cur
        return res

        