class Solution:
    def helper(self, nums, index, temp, target, res):
        if target == 0:
            res.append(temp[:])
            return
        
        for i in range(index, len(nums)):
            if nums[i] <= target:
                temp.append(nums[i])
                self.helper(nums, i, temp, target - nums[i], res)
                temp.pop()           # BACKTRACK

    def combinationSum(self, nums, target):
        nums.sort()                  # recommended, not required
        res = []
        self.helper(nums, 0, [], target, res)
        return res
