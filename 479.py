# 可以打表的暴力无聊题
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        for i in range(10**n-1, 10**(n-1), -1):
            j, num = i, i
            while(j):
                num = num * 10 + j % 10
                j //= 10
            maxp = 10**n-1
            num_sqrt = sqrt(num)
            while maxp > num_sqrt:
                if not num % maxp:
                    return num % 1337
                maxp -= 1