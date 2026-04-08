class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1 = len(word1)
        n2 = len(word2)
        mem = [[-1 for _ in range(n2)] for _ in range(n1)]
        def dfs(p1,p2):
            if p1>=n1 or p2>=n2:
                return abs(p1-n1)+abs(p2-n2)
            if mem[p1][p2]!= -1:
                return mem[p1][p2]
            if word1[p1]==word2[p2]:
                res = dfs(p1+1,p2+1)
            else:
                res= 1+min(dfs(p1,p2+1),dfs(p1+1,p2),dfs(p1+1,p2+1))
            mem[p1][p2]=res
            return res
    
        return dfs(0,0)
        