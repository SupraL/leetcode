class Solution(object):
    def my_int(self, s):
        result = 0
        curpos = len(s)
        for i in s:
            if curpos > 1:
                result += (ord(i) - 0x30) * (10 ** (curpos - 1))
                curpos -= 1
            else:
                result += (ord(i) - 0x30)
        return result
            
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(self.my_int(num1) * self.my_int(num2))
        