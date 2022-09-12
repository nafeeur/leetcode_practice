class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        prefix = suffix = 1
        for i, _ in enumerate(nums):
            answer[i] *= prefix
            answer[-i - 1] *= suffix
            prefix *= nums[i]
            suffix *= nums[-i - 1]
        
        return answer