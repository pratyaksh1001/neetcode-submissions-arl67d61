class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)

        i=0
        while i<len(nums):

            curr=nums[i]

            j=i+1

            while j<len(nums) and nums[j]==curr:
                j+=1
            
            if j-1+1>len(nums)//2:
                return curr
            else:
                i=j+1
        return -1