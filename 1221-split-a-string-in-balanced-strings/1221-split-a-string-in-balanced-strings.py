class Solution:
    def balancedStringSplit(self, s: str) -> int:
        nums = []
        sum = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "R":
                nums.append(1)
            elif s[i] == "L":
                nums.append(-1)
        for i in range(len(nums)):
            sum += nums[i]
            if sum == 0:
                count+=1
        return count  
        