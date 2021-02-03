class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if A == B:
            return True
        
        l = len(A)
        for i in range(l):
            A = A[-1] + A[:-1]
            if A == B:
                return True
        return False