class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for row in A:
            r = []
            for i in range(len(row)-1, -1, -1):
                r.append(row[i] ^ 1)
            result.append(r)
        return result