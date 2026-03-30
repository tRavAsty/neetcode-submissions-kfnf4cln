class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        mem = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                mem[i][j] = max(mem[i-1][j],mem[i][j-1],mem[i-1][j-1]+1 if text1[i-1]==text2[j-1] else 0)
        return mem[m][n]
        # if len(text1) <= 0 or len(text2) <= 0:
        #     return 0
        # return max(self.longestCommonSubsequence(text1,text2[:-1]),self.longestCommonSubsequence(text1[:-1],text2),self.longestCommonSubsequence(text1[:-1],text2[:-1])+1 if text1[-1]==text2[-1] else 0)

# bcat crabt
# first character, b!=c, return 0
# second character
# b cr return 0
# bc c return 1
# bc, cr LCS = 1
# bca, cr LCS = 1
# bc, cra LCS = 1
# bca, cra LCS = 2
        