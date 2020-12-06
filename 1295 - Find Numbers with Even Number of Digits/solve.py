class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for n in nums:
            c += 1 if len(str(n))%2 == 0 else 0
        return c