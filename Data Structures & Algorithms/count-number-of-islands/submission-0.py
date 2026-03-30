class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # init
        m,n = len(grid),len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        result = 0

        #traverse
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    queue = [(i,j)]
                    result +=1
                    while(len(queue)>0):
                        x,y = queue.pop()
                        if grid[x][y] == "1":
                            visited[x][y] = True
                        for delta_x,delta_y in dirs:
                            neighbor_x = x+delta_x
                            neighbor_y = y+delta_y
                            if neighbor_x>=0 and neighbor_x<m and neighbor_y>=0 and neighbor_y<n and grid[neighbor_x][neighbor_y]=="1" and not visited[neighbor_x][neighbor_y]:
                                queue.append((neighbor_x,neighbor_y))
        
        return result
                        


        