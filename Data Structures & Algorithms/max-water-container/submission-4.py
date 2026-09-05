class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        j=n-1
        res=0
        while i<=j:
            t=(j-i)*min(heights[i],heights[j])
            if t>res:
                res=t
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return res