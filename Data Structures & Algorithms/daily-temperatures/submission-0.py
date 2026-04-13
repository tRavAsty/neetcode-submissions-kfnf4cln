class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0 for _ in range(n)]
        stack = []
        stack.append((temperatures[n-1],n-1))
        for i in range(n-2,-1,-1):
            while stack and temperatures[i]>=stack[-1][0]:
                stack.pop()
            if stack:
                results[i]=stack[-1][1]-i
            stack.append((temperatures[i],i))
        return results
        