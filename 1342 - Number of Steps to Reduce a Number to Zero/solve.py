class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        bin(14) = 1110
        bin(7) = 1110
        bin(7-1) = 110
        bin(3) = 11
        """
        bn = bin(num)[2:]
        return (len(bn) - 1) + bn.count("1")