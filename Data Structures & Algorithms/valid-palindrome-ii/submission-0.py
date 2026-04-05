class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n-1

        def helper(start,end,allow):
            if start > end:
                return False

            if start == end:
                return True

            if start+1 == end:
                return s[start]==s[end] or allow
            
            if s[start]==s[end]:
                return helper(start+1,end-1,allow)
            else:
                if not allow:
                    return False
                return helper(start+1,end,not allow) or helper(start,end-1,not allow)
            
        return helper(0,n-1,True)

        