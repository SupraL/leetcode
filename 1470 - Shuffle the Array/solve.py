class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        r = []
        for x, y in zip(nums[:n], nums[n:]):
            r.extend([x, y])
        return r