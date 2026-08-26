class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        n=len(nums)
        t=[set() for _ in range(n+1)]
        res=[]
        d={}

        for i in range(n):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        
        for k,v in d.items():
            t[v].add(k)
        
        for i in range(n,-1,-1):
            if len(t[i])>0 and K>0:
                for j in t[i]:
                    res.append(j)
                    K-=1
        return res