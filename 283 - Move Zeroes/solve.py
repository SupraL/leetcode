class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0
        zero_count = 0
        while index < len(nums):
            if nums[index] == 0:
                del nums[index]
                index -= 1
                zero_count += 1
            index += 1
        nums += [0] * zero_count