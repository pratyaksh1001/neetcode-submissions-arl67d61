class Solution {

    public static int helper(int[][] grid,int[][] dp,int m,int n,int x,int y){
        if(x==m-1 && y==n-1){
            return 1;
        }
        if(x>=m || y>=n){
            return 0;
        }
        if(dp[x][y]!=-1){
            return dp[x][y];
        }
        if(grid[x][y]==1){
            return 0;
        }
        int w1=0,w2=0;
        

        if(x+1<m && grid[x+1][y]==0){
            w1=helper(grid,dp,m,n,x+1,y);
        }
        if(y+1<n && grid[x][y+1]==0){
            w2=helper(grid,dp,m,n,x,y+1);
        }
        dp[x][y]=w1+w2;
        return dp[x][y];
    }

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {

        if(obstacleGrid[0][0]==1){
            return 0;
        }

        int m=obstacleGrid.length;
        int n=obstacleGrid[0].length;
        
        int[][] dp=new int[m][n];

        for(int[] i:dp){
            Arrays.fill(i,-1);
        }
        return helper(obstacleGrid,dp,m,n,0,0);
    }
}