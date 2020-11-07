class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[-1] < target:
            return len(nums)

        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)