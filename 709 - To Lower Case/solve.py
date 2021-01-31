class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        for i in range(len(str)):
            ascii = ord(str[i])
            if 0x41 <= ascii <= 0x5A:
                str = str[:i] + chr(ascii + 0x20) + str[i+1:]
        return str