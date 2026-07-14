class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        h=n-1
        m=-1
        while l<h:
            if l==h:
                return nums[m]
            m=(l+h)//2
            if nums[m]>nums[h]:
                l=m+1
            else:
                h=m
        return nums[l]