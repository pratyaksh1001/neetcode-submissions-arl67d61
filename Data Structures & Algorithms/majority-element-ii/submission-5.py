class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        res=[]
        print(d)
        for i in d.keys():
            if d[i]>n//3:
                res.append(i)
        del d
        return res