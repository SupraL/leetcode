class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            index = 1
            while index < len(nums):
                if nums[index] == nums[index-1]:
                    del nums[index-1]
                    index -= 1
                index += 1