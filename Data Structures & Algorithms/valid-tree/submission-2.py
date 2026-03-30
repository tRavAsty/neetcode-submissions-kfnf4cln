class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        if n == 1:
            return True

        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = set()
        queue = deque([[0,-1]])
        visited.add(0)

        while queue:
            cur,parent = queue.popleft()
            for nei in adj[cur]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                queue.append([nei,cur])
        
        return len(visited)==n


        
        