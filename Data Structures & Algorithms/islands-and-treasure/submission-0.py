from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M = len(grid)
        N = len(grid[0])
        INF = 2**31-1
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    dist = 0
                    queue = deque([(i,j)])
                    visited = set()
                    while queue:
                        size = len(queue)
                        for _ in range(size):
                            r,c = queue.popleft() 
                            if r>=0 and r<M and c>=0 and c<N and (r,c) not in visited and grid[r][c]>=0:
                                grid[r][c] = min(grid[r][c],dist)
                                for d in dirs:
                                    queue.append((r+d[0],c+d[1]))
                                visited.add((r,c))
                        dist+=1
        


        