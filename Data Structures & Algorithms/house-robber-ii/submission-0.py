class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        def solve(arr):
            prev2 = 0
            prev1 = 0

            for money in arr:
                curr = max(prev1, money + prev2)
                prev2 = prev1
                prev1 = curr

            return prev1

        return max(solve(nums[:-1]),solve(nums[1:]))