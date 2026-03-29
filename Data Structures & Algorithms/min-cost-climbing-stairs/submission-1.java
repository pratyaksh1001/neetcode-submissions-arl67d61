class Solution {

    public int helper(int[] cost,int[] dp,int curr){
        

        if(dp[curr]!=0||curr<=1){
            return dp[curr];
        }

        int result=Math.min(helper(cost,dp,curr-1),helper(cost,dp,curr-2));
        dp[curr]=result+cost[curr];
        return dp[curr];
    }

    public int minCostClimbingStairs(int[] cost) {
        int n=cost.length;
        int[] dp=new int[n+1];
        dp[0]=cost[0];
        dp[1]=cost[1];
        if(n==2){
            return Math.min(dp[0],dp[1]);
        }
        return Math.min(helper(cost,dp,n-1),helper(cost,dp,n-2));

    }
}
