class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max=nums[0]
        curr_min=nums[0]
        n=len(nums)
        res=nums[0]

        for i in range(1,n):
            curr=nums[i]

            temp_max=max(curr,curr_max*curr,curr_min*curr)
            curr_min=min(curr,curr_max*curr,curr_min*curr)
            curr_max=temp_max
            res=max(curr_max,res)
        return res