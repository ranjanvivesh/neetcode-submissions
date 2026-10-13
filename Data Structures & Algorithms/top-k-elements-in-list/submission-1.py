class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        
        bucket = [[] for _ in range(len(nums) + 1)]

        
        for key, value in freq.items():
            bucket[value].append(key)

        
        result = []

        
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result



                    