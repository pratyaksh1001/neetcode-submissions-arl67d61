class Solution {

    public int dfs(int[][] grid, boolean[][] vis, int x, int y) {
        if (x < 0 || y < 0 || x >= grid.length || y >= grid[0].length || 
            vis[x][y] || grid[x][y] == 0) {
            return 0;
        }

        vis[x][y] = true;

        int area = 1;
        area += dfs(grid, vis, x + 1, y);
        area += dfs(grid, vis, x - 1, y);
        area += dfs(grid, vis, x, y + 1);
        area += dfs(grid, vis, x, y - 1);

        return area;
    }

    public int maxAreaOfIsland(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        boolean[][] vis = new boolean[n][m];
        int res = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!vis[i][j] && grid[i][j] == 1) {
                    int t = dfs(grid, vis, i, j);
                    res = Math.max(res, t);
                }
            }
        }

        return res;
    }
}
