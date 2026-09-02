from _heapq import heappush
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        heapq.heapify(h)
        for i in nums:
            heapq.heappush(h,-i)
        for i in range(k-1):
            heapq.heappop(h)
        return - heapq.heappop(h)