class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper = {}
        for i,x in enumerate(nums):
            key = target-x
            if key not in helper:
                helper[key] = [i]
            else:
                helper[key].append(i)
            
        for i,x in enumerate(nums):
            residue = target-x
            if x in helper:
                if residue!=x:
                    return [i,helper[x][0]]
                else:
                    if len(helper[x])>1:
                        return [i,helper[x][1]]
        
        return []




        