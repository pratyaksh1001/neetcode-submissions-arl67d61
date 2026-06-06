class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[-1]*(len(cost)+1)
        dp[0]=cost[0]
        if len(cost)>=1:
            dp[1]=cost[1]
        def helper(curr):
            if curr<0:
                return 2**31
            if dp[curr]!=-1:
                return dp[curr]
            res=min(helper(curr-1),helper(curr-2))
            dp[curr]=res+cost[curr]
            return dp[curr]
        return min(helper(len(cost)-1),helper(len(cost)-2))