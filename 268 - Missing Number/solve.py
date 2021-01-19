class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = len(nums) + 1
        return (s*(s-1) / 2) - sum(nums)