class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exist = [False for _ in range(n+1)]
        for i in range(n):
            exist[nums[i]] = True
        
        for i in range(n+1):
            if not exist[i]:
                return i
        return -1

        