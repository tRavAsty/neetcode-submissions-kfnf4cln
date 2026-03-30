class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for c in t:
            freq[c]=freq.get(c,0)+1
        
        n = len(s)
        l=0
        r=0
        min_l = float('inf')
        res = ""
        match = 0
        freq_cur = {}

        while r<n:
            c = s[r]
            if c in freq:
                freq_cur[c] = freq_cur.get(c,0)+1
                if freq_cur[c]<=freq[c]:
                    match+=1
                    if match == len(t):
                        while l<=r:
                            if s[l] in t:
                                if freq_cur[s[l]]==freq[s[l]]:
                                    break
                                else:
                                    freq_cur[s[l]]-=1
                            l+=1
                        if r-l+1<min_l:
                            res = s[l:r+1]
                            min_l = r-l+1
                        freq_cur[s[l]]-=1
                        l+=1
                        match-=1

            r+=1

        return res