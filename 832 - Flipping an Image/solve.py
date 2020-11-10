class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # Version 2: in place swap
        for row in A:
            l = 0
            r = len(row)-1
            while l <= r:
                row[l], row[r] = row[r] ^ 1, row[l] ^ 1
                l += 1
                r -= 1
        return A

        # Version1
        """result = []
        for row in A:
            r = []
            for i in range(len(row)-1, -1, -1):
                r.append(row[i] ^ 1)
            result.append(r)
        return result"""