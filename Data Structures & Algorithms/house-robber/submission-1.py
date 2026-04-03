class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        if len(nums)>1:
            dp[1]=nums[1]
        else:
            return dp[0]
        
        def helper(curr):
            if curr<0:
                return 0
            if dp[curr]!=0:
                return dp[curr]
            res=max(helper(curr-2),helper(curr-3))
            dp[curr]=res+nums[curr]
            return dp[curr]
            
        return max(helper(len(nums)-1),helper(len(nums)-2))