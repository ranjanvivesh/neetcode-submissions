class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers) - 1
        i = 0
        add = 0
        while i < j :
            add = numbers[i] + numbers[j]
            if add > target:
                j = j - 1
            elif add < target:
                i = i + 1
            else:
                return [i+1,j+1]        
        