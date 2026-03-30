class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ways = [0 for _ in range(n+1)]
        ways[0]=1
        for i in range(n):
            cur = s[i]
            if s[i] == '0':
                if i-1>=0:
                    num = int(s[i-1:i+1])
                    if 1<=num<=26:
                        ways[i+1]+=ways[i-1]
                else:
                    return 0
            elif '1'<=s[i]<='9':
                ways[i+1] += ways[i]
                if i-1>=0:
                    num = int(s[i-1:i+1])
                    if 11<=num<=26:
                        ways[i+1]+=ways[i-1]
            else:
                return 0
        return ways[n]

        