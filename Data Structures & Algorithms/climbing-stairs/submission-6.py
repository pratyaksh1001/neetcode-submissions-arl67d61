class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        dp[0]=1
        if n>=1:
            dp[1]=1

        def helper(curr):
            if curr<0:
                return 0
            if dp[curr]!=-1:
                return dp[curr]
            res=helper(curr-1)+helper(curr-2)
            dp[curr]=res
            return res
        return helper(n)