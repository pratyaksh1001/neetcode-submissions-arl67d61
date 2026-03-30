class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=[0]*n
        r=[0]*n
        lm=0
        rm=0

        i=0
        j=n-1
        res=0
        while i<=j:
            t=(j-i)*min(heights[i],heights[j])
            c=False
            if t>res:
                res=t
            
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1

            
        return res
