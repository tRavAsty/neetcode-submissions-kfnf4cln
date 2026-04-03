from collections import deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        mem = {}
        visited = [False for _ in range(n)]
        for i in range(n):
            ticket = tickets[i]
            dep = ticket[0]
            arr = ticket[1]
            if dep not in mem:
                mem[dep] = []
            mem[dep].append((i,arr))
        
        for dep in mem:
            mem[dep] = deque(sorted(mem[dep],key=lambda pair:pair[1]))
        
        res = ["JFK"]

        def dfs(path):
            if len(path) == n+1:
                return path
            if path[-1] not in mem:
                return None
            
            for index,des in mem[path[-1]]:
                if not visited[index]:
                    visited[index]=True
                    res = dfs(path+[des])
                    if res:
                        return res
                    visited[index]=False
            return None

        return dfs(res)


        