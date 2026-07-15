class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)

        def helper(curr,res):
            result.append(res[:])
            for i in range(curr,n):
                res.append(nums[i])
                helper(i+1,res)
                res.pop()
        helper(0,[])
        return result
        