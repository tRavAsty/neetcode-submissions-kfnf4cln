class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_height = [0 for _ in range(n)]
        right_height = [0 for _ in range(n)]
        left = height[0]
        right = height[-1]

        for i in range(1,n):
            bar = height[i]
            left_height[i] = left
            if bar>left:
                left = bar

        for i in range(n-2,-1,-1):
            bar = height[i]
            right_height[i] = right
            if bar>right:
                right = bar
        
        res = 0
        for i in range(1,n-1):
            h = min(left_height[i],right_height[i])
            if h-height[i]>0:
                res+=(h-height[i])
        return res
# left_height: 0,0,2,2,3,3,3,3,3,3
# right_height: 1,1,2,3,3,3,3,3,2


        