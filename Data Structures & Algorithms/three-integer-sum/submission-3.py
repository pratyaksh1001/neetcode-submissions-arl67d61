class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        result=[]
        n=len(nums)
        for i in range(n-2):
            j=i+1
            k=n-1
            while j < k :
                if nums[i]+nums[j]+nums[k]==0:
                    if [nums[i],nums[j],nums[k]] not in result:
                        result.append([nums[i],nums[j],nums[k]])
                    j+=1
                if nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        return result