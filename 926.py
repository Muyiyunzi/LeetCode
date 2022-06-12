# 这种也能dp是没想到的
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0, dp1 = 0, 0
        for i in s:
            dp0 = dp0 + (i == '1')
            dp1 = min(dp0 - (i == '1'), dp1) + (i == '0')
        return min(dp0, dp1)