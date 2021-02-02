class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) == 1 or k == 0:
            return nums
        nums[:0] = nums[-k:]
        nums[-k:] = []