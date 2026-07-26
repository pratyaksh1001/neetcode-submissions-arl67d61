class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = k - 1
        prefix = 0
        absdiff = [0] * len(arr)
        prefarr = [0] * len(arr)

        for i, v in enumerate(arr):
            absdiff[i] = abs(x - v)
            prefarr[i] = prefix + absdiff[i]
            prefix = prefarr[i]

        minsum = float("inf")
        minindex = float("inf")        
        
        #full size search space
        if k == len(arr):
            return arr

        store = []
        while r < len(arr):
            currsum = prefarr[r] - prefarr[l - 1] if l > 0 else prefarr[r]

            if minsum >= currsum:
                minsum = currsum
                store.append((minsum,l))
            r += 1
            l += 1

        #hacky AF
        for j in store:
            if j[0] == minsum:
                minindex = j[1]
                break

        return arr[minindex : minindex+k]