class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0
        for num in nums:
            if num == 1:
                count+=1
                if count >= maxcount:
                    maxcount = count
            if num == 0:
                count = 0        
        return maxcount        