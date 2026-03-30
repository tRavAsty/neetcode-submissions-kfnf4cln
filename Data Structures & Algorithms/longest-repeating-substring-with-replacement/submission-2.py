class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
        # res = 0
        # nums = {}
        # l,r=0,0
        # for r in range(len(s)):
        #     curr = s[r]
        #     if curr not in nums:
        #         nums[curr]=1
        #     else:
        #         nums[curr]+=1
        #         # (r-l+1)-max_num <=k
        #     max_num = max(nums.values())
        #     while (r - l + 1) - max_num > k:
        #         nums[s[l]] -= 1
        #         l += 1
        #         max_num = max(nums.values())
        #     res = max(res,r-l+1)
        #     r+=1
        # return res