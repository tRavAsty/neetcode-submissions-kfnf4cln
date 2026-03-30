class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            for j in range(i+1,n):
                containers = min(heights[i],heights[j])*(j-i)
                res = max(containers,res)
        return res
        