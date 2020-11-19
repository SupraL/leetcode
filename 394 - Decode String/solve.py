class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = ""
        stk = []
        
        while "[" in s:
            current = ""
            num = ""
            for c in s:
                if "0" <= c <= "9" and len(stk) == 0:
                    num += str(c)
                elif "a" <= c <= "z" and len(stk) == 0:
                    out += c
                elif c == "[":
                    num = int(num)
                    stk.append(c)
                    if len(stk) > 1:
                        current += c
                elif c == "]":
                    if len(stk) > 1:
                        current += c
                    else:
                        out += current * num
                        current = ""
                        num = ""
                    stk.pop()
                elif len(stk) > 0:
                    current += c
            s = out
            out = ""
        return s