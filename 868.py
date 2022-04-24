# 第一版。两个问题，一是总想着先转bin；二是没必要再用bool flag
class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)
        ind, ans, find = 0, 0, False
        for i, val in enumerate(s):
            if val != '1':
                continue
            elif not find:
                find = True
            elif find:
                ans = max(ans, i - ind)
            ind = i
        return ans

# 好吧，改写之后好像也没太大差异
class Solution:
    def binaryGap(self, n: int) -> int:
        last, ans, i = -1, 0, 0
        while n:
            if n & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
            n >>= 1
            i += 1
        return ans