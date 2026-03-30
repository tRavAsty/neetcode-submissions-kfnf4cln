class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        max_rob = [0 for _ in range(n+2)]
        for i in range(n):
            max_rob[i+2] = max(nums[i]+max_rob[i],max_rob[i+1])
        return max_rob[n+1]
        
        