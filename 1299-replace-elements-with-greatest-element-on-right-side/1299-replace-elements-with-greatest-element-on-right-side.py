class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = 0
        r = l+1
        maxI = 0
        def findMax(arr):
            maxInt = 0
            for i in arr:
                if i>maxInt:
                    maxInt = i
            return maxInt
        while l< len(arr)-1:
            maxI = findMax(arr[r:])
            arr[l] = maxI
            l+=1
            r+=1
        arr[-1] = -1
        return arr
            