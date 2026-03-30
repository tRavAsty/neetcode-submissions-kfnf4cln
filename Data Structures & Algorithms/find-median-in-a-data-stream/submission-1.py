class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap,num)
        else:
            if num>=self.max_heap[0]:
                heapq.heappush(self.max_heap,num)
            else:
                heapq.heappush(self.min_heap,-num)

            if len(self.max_heap)-len(self.min_heap)>1:
                tmp = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap,-tmp)
            
            if len(self.min_heap)>len(self.max_heap):
                tmp = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap,-tmp)

        print(self.max_heap)
        print(self.min_heap)
        

    def findMedian(self) -> float:
        if len(self.max_heap)>len(self.min_heap):
            return self.max_heap[0]
        print(self.max_heap)
        print(self.min_heap)
        return (self.max_heap[0]-self.min_heap[0])/2
        
        