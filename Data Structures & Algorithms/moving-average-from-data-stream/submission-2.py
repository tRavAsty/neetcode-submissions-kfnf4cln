class MovingAverage:

    def __init__(self, size: int):
        self.counter = 0
        self.vals = [0 for _ in range(size)]
        

    def next(self, val: int) -> float:
        size = len(self.vals)
        self.vals[self.counter%size] = val
        self.counter+=1

        if self.counter>=size:
            return sum(self.vals)/(0.0+size)
        else:
            return sum(self.vals)/(self.counter+0.0)


        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
