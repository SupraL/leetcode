class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bucket_mapping = {'}': '{', ')': '(', ']': '['}
        open_bucket_list = bucket_mapping.values()
        stack = []
        if len(s) < 2:
            return False
        for c in s:
            if c in open_bucket_list:
                stack.append(c)
            else:
                if len(stack) == 0 or bucket_mapping[c] != stack.pop():
                    return False
        return True if len(stack) == 0 else False