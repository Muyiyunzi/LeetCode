# 此题乘法原理最优解
# 纯打表
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851]
        return ans[n]

# 间接打表，慢4ms
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = [1, 9, 9*9, 9*9*8, 9*9*8*7, 9*9*8*7*6, 9*9*8*7*6*5, 9*9*8*7*6*5*4, 9*9*8*7*6*5*4*3]
        return sum(ans[:n+1])

# 乘法原理+动态规划
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = [1] * 9
        ans[1] = 9
        for i in range(2, 9):
            ans[i] = ans[i-1] * (11-i)
        return sum(ans[:n+1])