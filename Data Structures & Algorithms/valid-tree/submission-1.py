from collections import deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        q = deque([0])
        
        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append(neighbor)
        
        # Check if all nodes are connected
        return len(visited) == n