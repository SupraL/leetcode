class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i in range(1, 2**len(nums)):
            r = bin(i)[2:].zfill(len(nums))
            result.append([y for x, y in zip(list(r),nums) if x == "1"])
        return result