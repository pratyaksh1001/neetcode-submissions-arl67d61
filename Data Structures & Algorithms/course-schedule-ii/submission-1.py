class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i:0 for i in range(numCourses)}
        adj = {i:[] for i in range(numCourses)}
        res = []
        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)
        
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        finished = 0
        while q:
            crs = q.popleft()
            res.append(crs)
            finished += 1
            for pre in adj[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        
        if finished != numCourses:
            return []
        
        return res[::-1]