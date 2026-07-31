class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]

        for a,b in prerequisites:
            graph[b].append(a)

        visiting=set()

        def dfs(course):
            if course in visiting:
                return False
            if graph[course]==[]:
                return True

            visiting.add(course)

            for i in graph[course]:
                if not dfs(i):
                    return False

            visiting.remove(course)
            graph[course]=[]
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True