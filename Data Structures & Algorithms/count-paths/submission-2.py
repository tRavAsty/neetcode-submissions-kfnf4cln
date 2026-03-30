class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1]*n for _ in range(m)]
        for i in range(n-1)[::-1]:
            for j in range(m-1)[::-1]:
                memo[j][i] = memo[j+1][i]+memo[j][i+1]
        return memo[0][0]
        # if m < 1 or n < 1:
        #     return 0
        # if m == 1 or n == 1:
        #     return 1
        # return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        
        