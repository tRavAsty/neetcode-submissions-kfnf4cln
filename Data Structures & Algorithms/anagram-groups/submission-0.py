class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def index(s:str):
            counter = [0 for _ in range(26)]
            for c in s:
                counter[ord(c)-ord('a')]+=1
            return "_".join([str(c) for c in counter])
        
        memo = {}
        for s in strs:
            i = index(s)
            if i not in memo:
                memo[i] = [s]
            else:
                memo[i].append(s)
        
        res = []
        for v in memo.values():
            res.append(v)
        return res