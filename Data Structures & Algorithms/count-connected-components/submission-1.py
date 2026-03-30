class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = [set([i]) for i in range(n)]
        res = n

        def connect(a,b):
            if components[a] == components[b]:
                return 0

            if len(components[b])>len(components[a]):
                a,b = b,a
            components[a]|=(components[b])
            for i in components[b]:
                components[i]=components[a]

            return 1


        for edge in edges:
            res -= connect(edge[0],edge[1])

        return res
        