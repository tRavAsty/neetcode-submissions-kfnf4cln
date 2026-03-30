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
        have = 0
        need = len(freq)
        window = {}

        while r<n:
            c = s[r]
            if c in freq:
                window[c] = window.get(c,0)+1
                if window[c]==freq[c]:
                    have+=1
                while have == need:
                    if r-l+1<min_l:
                        res = s[l:r+1]
                        min_l = r-l+1

                    if s[l] in t:
                        if window[s[l]]==freq[s[l]]:
                            have-=1
                        window[s[l]]-=1
                    l+=1

            r+=1

        return res