class StockSpanner:

    def __init__(self):
        self.l=[]
        self.s=0
        self.curr=0

    def next(self, price: int) -> int:
        self.l.append(price)
        n=len(self.l)
        i=n-1
        r=0
        while i>=0:
            if self.l[i]<=price:
                r+=1
                i-=1
            else:
                break
        return r


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)