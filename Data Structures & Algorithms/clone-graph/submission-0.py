"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        queue = [node]
        while queue:
            curr = queue.pop()
            if curr not in visited:
                clone = Node(curr.val)
                visited[curr] = clone
                for n in curr.neighbors:
                    queue.append(n)


        queue = [node]
        visited2 = set()
        while queue:
            curr = queue.pop()
            if curr not in visited2:
                visited2.add(curr)
                new_neighbors = [visited[n] for n in curr.neighbors]
                visited[curr].neighbors = new_neighbors
                for n in curr.neighbors:
                    queue.append(n)

        return visited[node]
            
        