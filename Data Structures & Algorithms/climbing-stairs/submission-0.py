class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1
        cur = 1
        for i in range(1,n):
            cur = prev1+prev2
            prev1,prev2 = cur,prev1
        
        return cur

        