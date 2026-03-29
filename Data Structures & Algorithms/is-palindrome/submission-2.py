class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s.replace(" ","")
        n=len(s)
        i=0
        j=n-1

        while i<=j:
            if s[i].isalnum() and s[j].isalnum() and s[i]==s[j]:
                i+=1
                j-=1
            elif not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            else:
                return False
        return True
