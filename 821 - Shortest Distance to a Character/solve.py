class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        num_stack = [10**4] * len(s)
        last_index = -1
        
        for i in range(len(s)):
            if s[i] == c:
                num_stack[i] = 0
                for j in range(last_index+1, i):
                    num_stack[j] = min(num_stack[j], i-j)
                last_index = i
            else:
                if last_index != -1:
                    num_stack[i] = min(num_stack[i], abs(last_index - i))
        return num_stack