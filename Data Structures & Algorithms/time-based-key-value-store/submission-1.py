class TimeMap:

    def __init__(self):
        self.cache = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key]=[[value, timestamp]]
        else:
            self.cache[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache or self.cache[key][0][1] > timestamp:
            return ""
        nums = [item[1] for item in self.cache[key]]
        l = 0
        r = len(nums)-1
        print(nums)
        while l<r:
            mid = r-(r-l)//2
            print(f"{l},{r},{mid}")
            if nums[mid] == timestamp:
                return self.cache[key][mid][0]
            elif nums[mid] > timestamp:
                r = mid -1
            else:
                l = mid
            print(f"{l},{r}")
        
        return self.cache[key][l][0]
        
