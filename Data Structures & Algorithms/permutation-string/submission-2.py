class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n=len(s2)
        m=len(s1)

        for i in range(n-m+1):
            if sorted(s1)==sorted(s2[i:i+m]):
                return True
        return False