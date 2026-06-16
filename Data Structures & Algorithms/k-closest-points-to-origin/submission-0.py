import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq=[]
        for x,y in points:
            d=math.sqrt((x**2)+(y**2))
            heapq.heappush(pq,(d,(x,y)))
        
        res=[]
        for i in range(k):
            res.append(list(heapq.heappop(pq)[1]))
        return res