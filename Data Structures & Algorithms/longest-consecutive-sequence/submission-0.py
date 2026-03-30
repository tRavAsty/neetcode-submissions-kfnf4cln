class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = {}
        res = 0
        for num in sorted(nums):
            if num-1 in longest:
                longest[num] = max(longest.get(num,0),longest[num-1]+1)
            else:
                longest[num]=1
            print(longest)
            res = max(res, longest[num])
        return res

        