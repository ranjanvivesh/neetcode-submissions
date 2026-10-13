class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = {}

        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        repeated = missing = 0

        for num in range(1, n * n + 1):
            if freq.get(num, 0) == 2:
                repeated = num
            elif freq.get(num, 0) == 0:
                missing = num

        return [repeated, missing]