class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        n = len(nums)
        max_prev = float('-inf')
        for i in range(n):
            max_prev = max(max_prev+nums[i],nums[i])
            result = max(result, max_prev)
        return result


# [-1]
# max_prev = -inf, -1
# i= -inf, 0
# result = -inf, -1

# [2,-3,4,-2,2,1,-1,4]
# n = 8
# max_prev = -inf, 2, -1, 4, 2
# i= -inf, 0, 1, 2, 3,
# result = -inf, 2, 2, 4, 4
        