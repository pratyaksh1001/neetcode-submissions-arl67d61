class Solution {

    public static int helper(int[][] dp,int m,int n,int x,int y){
        if(x==m-1 && y==n-1){
            return 1;
        }
        if(x>=m || y>=n){
            return 0;
        }
        if(dp[x][y]!=-1){
            return dp[x][y];
        }
        int w1=helper(dp,m,n,x,y+1);
        int w2=helper(dp,m,n,x+1,y);
        dp[x][y]=w1+w2;
        return w1+w2;
    }


    public int uniquePaths(int m, int n) {
        int[][] dp=new int[m][n];
        for(int[] i:dp){
            Arrays.fill(i,-1);
        }
        return helper(dp,m,n,0,0);
    }
}
