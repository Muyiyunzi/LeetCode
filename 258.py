# 第一版暴力，O(logn)
class Solution:
    def addDigits(self, num: int) -> int:
        while(num // 10):
            L = list(str(num))
            num = 0
            for i in L:
                num += int(i)
        return num