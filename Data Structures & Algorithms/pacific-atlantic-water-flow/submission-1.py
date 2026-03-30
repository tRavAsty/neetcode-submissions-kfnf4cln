class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        m = len(heights)
        n = len(heights[0])

        queue1 = []
        queue2 = []
        for i in range(m):
            queue1.append((i,0))
            queue2.append((i,n-1))
        for j in range(n):
            queue1.append((0,j))
            queue2.append((m-1,j))
        
        def bfs(queue, visited):
            deltas = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue:
                coord = queue.pop()
                if coord not in visited:
                    visited.add(coord)
                    r,c = coord[0],coord[1]
                    h = heights[r][c]
                    for delta in deltas:
                        n_r = r+delta[0]
                        n_c = c+delta[1]
                        if n_r>=0 and n_r<m and n_c>=0 and n_c<n and heights[n_r][n_c]>=h:
                            queue.append((n_r,n_c))

        bfs(queue1, pacific)
        bfs(queue2, atlantic)

        res = []
        for element in pacific.intersection(atlantic):
            res.append(list(element))
        return res
        