# 第一版 手机上做的
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0: return '0'
        ans = ''
        flag = '-' if num < 0 else ''
        num=abs(num)
        while num:
            ans += str(num%7)
            num //= 7
        ans = ans[::-1]
        return flag + ans