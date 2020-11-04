class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        result = 1
        pervious = s[0]
        for c in s[1:]:
            count = count + 1 if c == pervious else 1
            if count > result:
                result = count
            pervious = c
        return result