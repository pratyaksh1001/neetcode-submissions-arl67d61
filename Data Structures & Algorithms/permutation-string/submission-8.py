class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s2)
        m=len(s1)
        if m>n:
            return False
        m1=[0]*26
        m2=[0]*26
        for i in s1:
            m1[ord(i)-ord("a")]+=1
        for i in range(m):
            m2[ord(s2[i])-ord("a")]+=1
        i=0
        j=m-1
        print(m1)
        while j<n:
            print(m2)
            if m1==m2:
                return True
            m2[ord(s2[i])-ord("a")]-=1
            i+=1
            j+=1
            if j<n:
                m2[ord(s2[j])-ord("a")]+=1

            
        return False