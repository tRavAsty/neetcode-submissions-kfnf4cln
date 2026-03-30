class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # max_rob = [0 for _ in range(n+2)]
        # for i in range(n):
        #     max_rob[i+2] = max(nums[i]+max_rob[i],max_rob[i+1])
        # return max_rob[n+1]
        max_rob = 0
        rob_prev = 0
        rob_prev_prev = 0
        for i in range(n):
            max_rob = max(nums[i]+rob_prev_prev, rob_prev)
            rob_prev, rob_prev_prev = max_rob, rob_prev
        return max_rob

        
        