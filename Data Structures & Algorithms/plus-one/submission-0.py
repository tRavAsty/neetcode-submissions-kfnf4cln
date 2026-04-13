class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carrier = 1
        n = len(digits)
        result = [0]*n
        for i in range(n-1,-1,-1):
            tmp=digits[i]+carrier
            result[i] = tmp%10
            carrier = tmp//10
        if carrier:
            result = [1]+result
        return result

            

        