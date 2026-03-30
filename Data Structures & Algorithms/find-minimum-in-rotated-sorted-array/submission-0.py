class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n-1
        while start<end:
            mid = start + (end-start)//2
            if nums[mid]<nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]
        