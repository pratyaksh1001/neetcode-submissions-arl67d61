class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n

        def helper(curr):
            
            if curr>=n:
                return 0
            if dp[curr]:
                return dp[curr]
            res=max(helper(curr+2),helper(curr+3))
            dp[curr]=res+nums[curr]
            return dp[curr]
        return max(helper(0),helper(1))