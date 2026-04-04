class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2!=0:
            return False
        target = target/2
        n = len(nums)
        def dfs(i,cur):
            if i>=n:
                return False
            if cur==target:
                return True
            if dfs(i+1,cur+nums[i]):
                return True
            if dfs(i+1,cur):
                return True
            return False
        return dfs(0,0)

        
        