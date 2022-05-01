# 被str(ans)坑到了
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        for i, val in enumerate(number):
            if val == digit:
                ans = max(ans, int(number[:i] + number[i+1:]))
        return str(ans)