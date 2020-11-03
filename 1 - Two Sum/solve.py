class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(list(enumerate(nums)), key=lambda x:x[1])
        for i in range(len(sorted_nums)):
            for j in range(i+1, len(sorted_nums)):
                ans = sorted_nums[i][1] + sorted_nums[j][1]
                if ans > target:
                    break
                if ans == target:
                    return [sorted_nums[i][0], sorted_nums[j][0]]