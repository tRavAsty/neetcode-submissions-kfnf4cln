class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1+n2 != n3:
            return False

        if (s1 == "" and s2==s3) or (s2=="" and s1==s3):
            return True
        p1 = 0
        p2 = 0
        while  p1<n1 and s3[p1]==s1[p1]:
            p1+=1

        while p2<n2 and s3[p2]==s2[p2]:
            p2+=1
            
        return (p1>0 and self.isInterleave(s1[p1:],s2,s3[p1:])) or (p2>0 and self.isInterleave(s1,s2[p2:],s3[p2:]))




        #abed
        #adbc
        #a ad b bc ed
        #ad ab bc ed
        