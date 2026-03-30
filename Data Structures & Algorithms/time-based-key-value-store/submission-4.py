class TimeMap:

    def __init__(self):
        self.mem = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mem:
            self.mem[key] = []
        self.mem[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mem or self.mem[key][0][0]>timestamp:
            return ""
        nums = self.mem[key]
        lo = 0
        hi = len(nums)-1
        while lo<hi:
            mid = hi-(hi-lo)//2
            if nums[mid][0]<=timestamp:
                lo =mid
            else:
                hi = mid-1
        return nums[lo][1]


        
