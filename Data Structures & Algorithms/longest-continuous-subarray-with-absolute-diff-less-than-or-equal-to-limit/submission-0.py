class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        l,r = 0,0
        res = 1
        cur_max = nums[0]
        cur_min = nums[0]
        while r<n:
            cur = nums[r]
            cur_max = max(cur,cur_max)
            cur_min = min(cur,cur_min)
            while cur_max-cur_min>limit:
                l+=1
                cur_max = max(nums[l:r+1])
                cur_min = min(nums[l:r+1])

            else:
                res = max(res,r-l+1)
            r+=1
        return res
