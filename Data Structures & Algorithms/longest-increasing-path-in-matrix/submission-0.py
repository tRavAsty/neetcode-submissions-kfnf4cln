class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(row,col,paths):
            if row<0 or row>=M or col<0 or col>=N or (paths and matrix[row][col]<=matrix[paths[-1][0]][paths[-1][1]]):
                return 0
            dirs = [(0,1),(1,0),(0,-1),(-1,0)]
            res = 1
            for delta in dirs:
                next_row = row+delta[0]
                next_col = col+delta[1]
                if (next_row,next_col) not in paths:
                    res = max(res,1+dfs(next_row,next_col,paths+[(row,col)]))
            return res
                

        M = len(matrix)
        N = len(matrix[0])
        res = 1
        for i in range(M):
            for j in range(N):
                res = max(res,dfs(i,j,[]))
        
        return res
        