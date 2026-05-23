class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=[set() for _ in range(n)]
        vis=set()

        for start,end in edges:
            graph[start].add(end)
            graph[end].add(start)

        def dfs(curr):
            vis.add(curr)

            for i in graph[curr]:
                if i not in vis:
                    dfs(i)

        c=0
        for i in range(n):
            if i not in vis:
                c+=1
                vis.add(i)
                dfs(i)
        return c