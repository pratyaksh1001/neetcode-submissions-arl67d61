class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l=[]
        r=[]
        lm=0
        rm=0
        for i in height:
            lm=max(i,lm)
            l.append(lm)
        for i in height[::-1]:
            rm=max(i,rm)
            r.append(rm)
        r=r[::-1]
        i=0
        j=0
        res=0
        print(l)
        print(r)
        for i in range(n):
            res+=min(l[i],r[i])-height[i]
        return res