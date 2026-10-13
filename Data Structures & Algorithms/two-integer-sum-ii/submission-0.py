class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = i+1
            for j in range(len(numbers)):
                add = numbers[i] + numbers[j]
                if add == target:
                    return [i+1,j+1]
                elif add > target:
                    numbers.pop()

        