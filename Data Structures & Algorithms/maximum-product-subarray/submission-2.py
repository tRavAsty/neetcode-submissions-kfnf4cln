class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_pos = 1
        prev_neg = 1
        res = nums[0]
        for num in nums:
            curr_pos = max(prev_pos*num,num,prev_neg*num) 
            curr_neg = min(prev_pos*num,num,prev_neg*num)
            res = max(curr_pos,curr_neg,res)
            prev_pos,prev_neg = curr_pos,curr_neg
        return res
        
# pos -inf, max(-inf,-2)=-2, max(-2*-1,-1)=2
# neg inf, min(inf,-2) = -2, min(-2*-1,-1) = -1
# res -inf, -2, 2