class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        buys = [0 for _ in range(n)]
        sells = [0 for _ in range(n)]
        buys[0] = prices[0]
        sells[n-1] = prices[n-1]
        for i in range(1, n):
            buys[i] = min(prices[i],buys[i-1])
        for i in range(n-2,0,-1):
            sells[i] = max(prices[i],sells[i+1])
        
        for i in range(n):
            res = max(res,sells[i]-buys[i])
        return res
        
            


        
        