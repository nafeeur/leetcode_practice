class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #Understanding - When input empty return None
        #When input len == 1 return the interval
        #The input can be unsorted 
        
        #Match - Sort the input 
        #plan - if end value of the first interval is > the start value pf second interval then merge 
        
        intervals.sort()
        mergedArr = []
        for i in intervals:
            if len(mergedArr) == 0:
                mergedArr.append(i)
            elif mergedArr[-1][-1] >= i[0]:
                if mergedArr[-1][-1] > i[-1]:
                    continue
                mergedArr[-1][-1] = i[-1]
            else:
                mergedArr.append(i)
            
        return mergedArr
        
        