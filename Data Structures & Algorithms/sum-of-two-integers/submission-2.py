class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        for digit in range(32):
            last_a = (a >> digit) & 1
            last_b = (b >>digit) &1
            cur = last_a ^ last_b ^ carry
        
            if last_a & last_b or ((last_a^last_b) & carry):
                carry = 1
            else:
                carry = 0
            if cur:
                res |= (1 << digit)
        
        if res > 0x7FFFFFFF:
            res = ~(res^0xFFFFFFFF)
        return res