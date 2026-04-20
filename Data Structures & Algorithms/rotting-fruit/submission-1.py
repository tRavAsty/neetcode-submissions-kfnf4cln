class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = -1
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        queue = deque([])
        fresh = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh.add((i,j))
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            l = len(queue)
            for i in range(l):
                x,y = queue.popleft()
                if (x,y) in fresh:
                    fresh.remove((x,y))
                for dir_x,dir_y in dirs:
                    new_x = x+dir_x
                    new_y = y+dir_y
                    if new_x>=0 and new_x<m and new_y>=0 and new_y<n and not visited[new_x][new_y] and grid[new_x][new_y]==1:
                        queue.append((new_x,new_y))
                        visited[new_x][new_y]=True
            res+=1
        
        if len(fresh)==0:
            return res if res>0 else 0
        else:
            return -1

                


        