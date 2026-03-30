class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        digit = 0
        tmp = n
        while tmp>0:
            tmp = tmp>>1
            digit+=1
        
        res = [0,1]
        for i in range(1,digit):
            res = res + [x+1 for x in res]
        return res[:n+1]

        