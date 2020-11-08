class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 1
        result = nums[0]
        nums_count = {nums[0]: 1}
        for n in nums[1:]:
            if n not in nums_count:
                nums_count[n] = 1
            else:
                nums_count[n] += 1
                if nums_count[n] > max_count:
                    max_count = nums_count[n]
                    result = n
        return result