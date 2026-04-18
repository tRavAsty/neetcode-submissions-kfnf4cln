class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [float('inf')]*(n+1)
        dp[0]=0
        for i in range(n):
            longest = min(i+nums[i],n-1)
            for j in range(i+1,longest+1):
                dp[j]=min(dp[j],dp[i]+1)
        return dp[n-1]
        