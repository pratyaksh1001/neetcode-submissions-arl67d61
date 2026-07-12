class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        n=len(prices)
        m=float("inf")
        for i in range(n-1):
            if prices[i]>prices[i+1]:
                i+=1
            else:
                profit+=prices[i+1]-prices[i]
        return profit