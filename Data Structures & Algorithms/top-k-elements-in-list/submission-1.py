from heapq import heappush,heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = []
        for num in nums:
            freq[num]+=1

        for key in freq:
            heappush(heap,(freq[key],key))
            if len(heap)>k:
                heappop(heap)
        
        return [item[1] for item in heap]
        
        