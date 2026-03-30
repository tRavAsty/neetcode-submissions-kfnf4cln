class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]
        left_product = [1 for _ in range(n)]
        right_product = [1 for _ in range(n)]
        for i in range(1,n):
            left_product[i] = left_product[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1):
            right_product[i] = right_product[i+1]*nums[i+1]
        
        for i in range(n):
            res[i] = left_product[i]*right_product[i]

        return res