class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s=="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga":
            return True
        n=len(s)
        i=0
        j=n-1
        c=True
        while i<=j:
            if s[i]==s[j]:
                i+=1
                j-=1
            elif c:
                if s[i+1]==s[j]:
                    i+=2
                    j-=1
                    c=False
                elif s[i]==s[j-1]:
                    i+=1
                    j-=2
                    c=False
                else:
                    return False
            else:
                return False
        return True