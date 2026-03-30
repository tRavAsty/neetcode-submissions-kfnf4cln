class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        tmp = [nums[i],nums[j],nums[k]]
                        tmp.sort()
                        id = f"{tmp[0]}_{tmp[1]}_{tmp[2]}"
                        if id not in seen:
                            res.append(tmp)
                            seen.add(id)
        
        return res



        