class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        res = []        
        for key,value in hashmap.items():
            if value > len(nums) // 3:
                res.append(key)
        return res           