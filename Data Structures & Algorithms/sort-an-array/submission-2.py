class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr):
            if len(arr) == 1: 
                return arr
            m = len(arr) // 2
            arr1 = mergeSort(arr[:m])
            arr2 = mergeSort(arr[m:])
            final = []
            for elem in arr1:
                while arr2 and arr2[0] <= elem:                
                    final.append(arr2[0])
                    del arr2[0]
                final.append(elem)
            final += arr2
            return final
        return mergeSort(nums)