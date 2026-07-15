class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]

        n=len(nums)
        res=[]
        s=set()
        def helper():
            if len(res)==n:
                result.append(res[:])
                return
            for i in nums:
                if i in s:
                    continue
                res.append(i)
                s.add(i)
                helper()
                s.remove(i)
                res.pop()
        helper()
        return result