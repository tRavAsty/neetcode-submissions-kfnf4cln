class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        power = abs(n)

        while power:
            if power%2==1:
                res *= x
            x*=x
            power = power//2

        if n<0:
            res = 1/res
        return res
        