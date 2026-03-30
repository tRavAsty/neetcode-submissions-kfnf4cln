class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        s = str(x)
        n = len(s)
        l = 0
        r = n-1

        while r>=l:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
            
        return True
        