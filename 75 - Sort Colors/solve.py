class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        r_map = {0:0, 1:0, 2:0}
        for n in nums:
            r_map[n] += 1
        nums[:r_map[0]] = [0]*r_map[0]
        nums[r_map[0]:r_map[1]+1] = [1]*r_map[1]
        nums[r_map[0]+r_map[1]:] = [2]*r_map[2]
        