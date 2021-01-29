class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        high = len(height) - 1
        
        max_water = 0
        while low != high:
            cur_water = min(height[low], height[high]) * (high-low)
            max_water = cur_water if cur_water > max_water else max_water
            if height[low] > height[high]:
                high -= 1
            else:
                low += 1
        return max_water