class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1] * m for _ in range(n)]  # fix #2

        def helper(i, j):
            if i >= n or j >= m:            # fix #1
                return 2**31
            if dp[i][j] != -1:
                return dp[i][j]
            if i == n-1 and j == m-1:      # fix #1 & #3
                dp[i][j] = grid[i][j]
                return dp[i][j]
            w1 = helper(i + 1, j)
            w2 = helper(i, j + 1)
            dp[i][j] = grid[i][j] + min(w1, w2)  # fix #4
            return dp[i][j]

        return helper(0, 0)  # also: just return directly