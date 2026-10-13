class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0
        i = 0
        j = len(height) - 1
        maxLeft, maxRight = height[i], height[j]
        area = 0
        while (i<j):
            if maxLeft < maxRight:
                i += 1
                maxLeft = max(maxLeft,height[i])
                area += maxLeft - height[i]
            else:
                j -= 1
                maxRight = max(maxRight,height[j])
                area += maxRight - height[j]     

        return area        
