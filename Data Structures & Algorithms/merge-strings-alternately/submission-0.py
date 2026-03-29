class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r=""

        n=len(word1)
        m=len(word2)

        i=0
        j=0
        while i<n and j<m:
            r+=word1[i]
            r+=word2[j]
            i+=1
            j+=1
        r+=word1[i:]
        r+=word2[j:]
        return r