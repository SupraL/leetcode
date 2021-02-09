class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        result = ""
        has_symbol = False
        has_number = False
        
        LOWER_BOUND = -2**31
        UPPER_BOUND = (2**31) - 1
        for c in s:
            if c == "-" or c == "+":
                if has_number:
                    break
                if not has_symbol and not has_number:
                    has_symbol = True
                    result += c
                    continue
                return 0
            elif "0" <= c <= "9":
                result += c
                has_number = True
                continue
            break
        if not has_number:
            return 0
        
        ret = 0
        tmp = result[1:] if has_symbol else result
        for i in range(len(tmp)):
            ret += (ord(tmp[~i]) - 0x30) * (10**(i))
        ret = ~ret + 1 if result[0] == "-" else ret
        if LOWER_BOUND < ret < UPPER_BOUND:
            return ret
        else:
            return LOWER_BOUND if ret < 0 else UPPER_BOUND