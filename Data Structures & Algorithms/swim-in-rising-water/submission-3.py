class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # dp = [[float('inf')]*n for _ in range(m)]
        # dp[0][0] = grid[0][0]
        l = max(grid[0][0],grid[m-1][n-1])
        r = max(map(max,grid))
       
        def connected(level):
            queue = deque([(0,0)])
            visited = set()
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]
            while queue:
                x,y = queue.popleft()
                if x==m-1 and y==n-1:
                    return True
                for dir_x,dir_y in dirs:
                    new_x = x+dir_x
                    new_y = y+dir_y
                    if new_x>=0 and new_x<m and new_y>=0 and new_y<n and (new_x,new_y) not in visited and grid[x][y]<=level:
                        queue.append((new_x,new_y))
                        visited.add((new_x,new_y))
            return False
        
        while l < r:
            mid = (l + r) // 2
            if connected(mid):
                r = mid
            else:
                l = mid + 1
        return l
