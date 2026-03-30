class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        rob1 = [0 for _ in range(n)]
        rob2 = [0 for _ in range(n)]
        #exclude head
        #exclude tail
        res = 0
        for i in range(1,n):
            rob1[i] = max(rob1[i-1], rob1[i-2]+nums[i] if i-2>=0 else nums[i])
            res = max(res,rob1[i])
        
        for i in range(n-1):
            rob2[i] = max(rob2[i-1],rob2[i-2]+nums[i] if i-2>=0 else nums[i])
            res = max(res,rob2[i])
        return res