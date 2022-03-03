# 第一版暴力，O(logn)
class Solution:
    def addDigits(self, num: int) -> int:
        while(num // 10):
            L = list(str(num))
            num = 0
            for i in L:
                num += int(i)
        return num

# 第二版 数学 O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        if num % 9 == 0:
            return 9 if num !=0 else 0
        else:
            return num % 9