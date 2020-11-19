class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        odd_max = 0
        even_max = 0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                even_max = max(even_max + nums[i], odd_max)
            else:
                odd_max = max(odd_max + nums[i], even_max)
        return max(even_max, odd_max)