class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=[0 for _ in range(n)]
        t=prices[0]
        l[0]=prices[0]
        for i in range(n):
            t=min(t,prices[i])
            l[i]=t
        i=n-1
        res=0
        print(l)
        while i>=1:
            res=max(res,prices[i]-l[i-1])
            i-=1
        return res