class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_jump = 0
        jumpable = [False for _ in range(n)]
        for i in range(n):
            if i<=max_jump:
                max_jump = max(i+nums[i],max_jump)
        return max_jump>=n-1
        