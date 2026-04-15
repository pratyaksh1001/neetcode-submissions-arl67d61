from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = []
        vis = set()
        p = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
                    vis.add((i, j))

                    while q:
                        x, y = q.pop(0)

                        # Down
                        if x + 1 < n:
                            if grid[x + 1][y] == 1:
                                if (x + 1, y) not in vis:
                                    vis.add((x + 1, y))
                                    q.append((x + 1, y))
                            else:
                                p += 1
                        else:
                            p += 1

                        # Right
                        if y + 1 < m:
                            if grid[x][y + 1] == 1:
                                if (x, y + 1) not in vis:
                                    vis.add((x, y + 1))
                                    q.append((x, y + 1))
                            else:
                                p += 1
                        else:
                            p += 1

                        # Up
                        if x - 1 >= 0:
                            if grid[x - 1][y] == 1:
                                if (x - 1, y) not in vis:
                                    vis.add((x - 1, y))
                                    q.append((x - 1, y))
                            else:
                                p += 1
                        else:
                            p += 1

                        # Left
                        if y - 1 >= 0:
                            if grid[x][y - 1] == 1:
                                if (x, y - 1) not in vis:
                                    vis.add((x, y - 1))
                                    q.append((x, y - 1))
                            else:
                                p += 1
                        else:
                            p += 1

                    return p