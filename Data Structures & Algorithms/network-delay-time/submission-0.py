import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = {}
        distance = [float('inf') for _ in range(n+1)]
        visited = set()
        for time in times:
            ui,vi,ti = time
            n = neighbors.get(ui,{})
            n[vi] = ti
            neighbors[ui] = n
        
        heap = [(0,k)]
        distance[k] = 0

        while heap:
            _, cur = heapq.heappop(heap)
            if cur not in visited:
                visited.add(cur)
                if cur in neighbors:
                    for n in neighbors[cur]:
                        distance[n] = min(distance[n],distance[cur]+neighbors[cur][n])
                        if n not in visited:
                            heapq.heappush(heap,(distance[n],n))

        
        res = max(distance[1:])
        return res if res!=float('inf') else -1



        