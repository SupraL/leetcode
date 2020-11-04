class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = {}
        for n in nums:
            if n not in tmp:
                tmp[n] = 1
            else:
                tmp[n] += 1
        sorted_dict = sorted(tmp.items(), key=lambda x:x[1])
        return sorted_dict[0][0]