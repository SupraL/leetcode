class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        for c in s:
            if (c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or (c >= "0" and c <= "9"):
                lst.append(c.lower())
        lst_s = "".join(lst)
        return lst_s == lst_s[::-1]