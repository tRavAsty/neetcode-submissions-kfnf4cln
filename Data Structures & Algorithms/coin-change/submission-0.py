class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        nums = [-1 for _ in range(amount+1)]
        nums[0] = 0
        for coin in coins:
            if coin<=amount:
                nums[coin] = 1
        for i in range(1, amount+1):
            for coin in coins:
                if i>=coin and nums[i-coin]!=-1:
                    if nums[i]!=-1:
                        nums[i] = min(nums[i],nums[i-coin]+1)
                    else:
                        nums[i] = nums[i-coin]+1
        return nums[amount]        