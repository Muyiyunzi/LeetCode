class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        na = len(a)
        nb = len(b)
        if na == nb:
            if a == b:
                return -1
            else:
                return na
        else: return na if na > nb else nb