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
        visited[node] = Node(node.val)
        while queue:
            curr = queue.pop()
            for n in curr.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    queue.append(n)
                visited[curr].neighbors.append(visited[n])

        return visited[node]
            
        