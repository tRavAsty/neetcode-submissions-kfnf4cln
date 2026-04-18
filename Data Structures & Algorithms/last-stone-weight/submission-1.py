class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        n = len(stones)
        for i in range(n):
            heapq.heappush(heap,-stones[i])
        cur = 0

        while heap:
            stone = -heapq.heappop(heap)
            if cur ==0:
                cur = stone
            else:
                cur = abs(cur-stone)
                heapq.heappush(heap,-cur)
                cur = 0
        return cur


        