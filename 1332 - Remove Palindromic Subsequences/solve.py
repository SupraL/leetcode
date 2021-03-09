class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        return 1 if s == s[::-1] else 2