class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = 0, -1
        while col < len(matrix[0]) and row < len(matrix):
            if matrix[row][col] == target:
                return True
            if matrix[row][0] <= target <= matrix[row][-1]:
                col += 1
            else:
                row += 1
        return False