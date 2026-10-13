class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):

            product = 1

            cp = nums.copy()

            del cp[i]

            for val in cp:
                product *= val

            result.append(product)
        return result