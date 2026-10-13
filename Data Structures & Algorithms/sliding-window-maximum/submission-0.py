class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count = 0
        check = []
        result = []
        for r in range(len(nums)):
            check.append(nums[r])
            if len(check)==k :
                result.append(max(check))
                check.pop(0)
        return result        