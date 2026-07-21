class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def solve(arr):
            m = len(arr)
            dp = [-1] * m
            def helper(curr):
                if curr >= m:
                    return 0
                if dp[curr] != -1:
                    return dp[curr]
                dp[curr] = arr[curr] + max(helper(curr + 2),helper(curr + 3))
                return dp[curr]
            return max(helper(0), helper(1))
        return max(solve(nums[:-1]),solve(nums[1:]))