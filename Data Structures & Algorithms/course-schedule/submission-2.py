class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        def has_loop(node):
            if node in visiting:
                return True
            visiting.add(node)
            for adj_node in adj[node]:
                if has_loop(adj_node):
                    return True
            visiting.remove(node)
            return False

        for i in range(numCourses):
            if adj[i]:
                if has_loop(i):
                    return False
        return True

        
        


        