class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # CRITICAL: Sort first!
        n = len(candidates)
        
        def dfs(i, path, goal):
            if goal < 0:
                return
            if goal == 0:
                res.append(path.copy())
                return
            if i >= n:
                return
            
            # Include candidates[i]
            path.append(candidates[i])
            dfs(i + 1, path, goal - candidates[i])
            path.pop()
            
            # Skip candidates[i] AND all its duplicates
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, path, goal)
        
        dfs(0, [], target)
        return res