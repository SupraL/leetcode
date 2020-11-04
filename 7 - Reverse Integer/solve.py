class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = str(x)[0] == "-" or str(x)[-1] == "-"
        ans = str(x)[::-1].replace("-", "")
        ans = int("-" + ans) if is_negative else int(ans)
        return ans if ans < 2**31 and ans > -2**31 else 0