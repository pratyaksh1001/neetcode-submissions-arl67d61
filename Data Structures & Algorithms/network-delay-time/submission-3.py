import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res=[float("inf") for _ in range(n+1)]
        res[0]=-1
        res[k]=0
        graph=[[float("inf") for _ in range(n+1)] for _ in range(n+1)]
        
        for u,v,t in times:
            graph[u][v]=t
        
        pq=[]
        pq.append((0,k))
        vis=set()
        while pq and len(vis)<n:
            t,curr=heapq.heappop(pq)
            if curr in vis:
                continue
            vis.add(curr)
            for i in range(1,n+1):
                n_t=graph[curr][i]
                if n_t==float("inf"):
                    continue
                if i!=curr and t+n_t<=res[i]:
                    heapq.heappush(pq,(t+n_t,i))
                    res[i]=t+n_t
        r=max(res)
        print(res)
        if r==float("inf"):
            return -1
        return int(r)