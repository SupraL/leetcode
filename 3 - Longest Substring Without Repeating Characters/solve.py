class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        low, high = 0, 0
        tmp_dict = {}
        max_count = 1
        
        if len(s) == 0:
            return 0
        
        while high < len(s):
            if s[high] not in tmp_dict:
                tmp_dict[s[high]] = high
                high += 1
                max_count = max(max_count, len(tmp_dict))
            else:
                del tmp_dict[s[low]]
                low += 1
        return max_count