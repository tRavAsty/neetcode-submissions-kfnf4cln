class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*n
        even = 0
        odd = n-1
        for num in nums:
            if num%2==0:
                arr[even]=num
                even+=1
            else:
                arr[odd]=num
                odd-=1
        return arr

        