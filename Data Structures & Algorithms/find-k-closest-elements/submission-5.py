class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        res=arr[:k]
        r=2**31
        for i in range(len(arr)-k+1):
            temp=arr[i:i+k]
            s=0
            for i in temp:
                s+=abs(i-x)
            s=s/k
            if s<r:
                r=s
                res=temp
        return res
