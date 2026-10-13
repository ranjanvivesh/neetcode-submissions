class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(set(nums))

        current_count = 1
        longest = 1

        for i in range(len(nums) - 1):

            if nums[i + 1] == nums[i] + 1:
                current_count += 1
            else:
                current_count = 1

            if current_count >= longest:
                 longest = current_count

        return longest