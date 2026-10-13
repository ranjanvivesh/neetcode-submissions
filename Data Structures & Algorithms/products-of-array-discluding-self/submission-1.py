class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums)+1)
        prefix[0] = 1
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]
        postfix = [1] * (len(nums) + 1)    
        for j in range(len(nums) - 1, -1, -1):
            postfix[j] = postfix[j+1] * nums[j]
        output = [1] * len(nums)
        for k in range(len(nums)):
            output[k] = prefix[k] * postfix[k+1]
        return output            