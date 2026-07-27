class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        right=[1]*n
        l=1
        r=1
        for i in range(n):
            l*=nums[i]
            left[i]=l
        for i in range(n-1,-1,-1):
            r*=nums[i]
            right[i]=r
        res=[1]*n
        print(left)
        print(right)
        for i in range(n):
            if i-1>=0:
                res[i]*=left[i-1]
            if i+1<n:
                res[i]*=right[i+1]
        return res