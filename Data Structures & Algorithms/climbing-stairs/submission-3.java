class Solution {

    public static int helper(int[] dp,int curr){
        if(curr<=1){
            return 1;
        }
        if(dp[curr]!=0){
            return dp[curr];
        }
        int result=helper(dp,curr-1)+helper(dp,curr-2);
        dp[curr]=result;
        return result;

    }

    public int climbStairs(int n) {
        if(n==1){
            return 1;
        }
        int[] dp=new int[n+1];
        dp[0]=0;
        dp[1]=1;
        return helper(dp,n);
    }
}
