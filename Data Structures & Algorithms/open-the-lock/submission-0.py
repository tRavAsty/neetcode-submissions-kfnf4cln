from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        queue = deque([("0000",0)])
        while queue:
            cur,step = queue.popleft()
            if cur == target:
                return step
            if cur in visited or cur in deadends:
                continue
            visited.add(cur)
            for i in range(4):
                digit = int(cur[i])
                half1 = cur[:i]
                half2 = cur[i+1:]
                forward = str((digit+1) %10)
                backward = str((digit-1)%10)
                queue.append((f"{half1}{forward}{half2}",step+1))
                queue.append((f"{half1}{backward}{half2}",step+1))
            
        return -1

        