class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph=[set() for _ in range(n)]
        graph_2=[set() for _ in range(n)]
        for link in trust:
            a=link[0]
            b=link[1]
            graph[b-1].add(a)
            graph_2[a-1].add(b)
        print(graph)
        for i in range(n):
            if len(graph[i])==n-1 and len(graph_2[i])==0:
                return i+1
        return -1