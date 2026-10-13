class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in range(0,len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        for key,value in freq.items():
            if value > 1:
                return True
                break
        
        return False         