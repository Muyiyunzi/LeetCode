# O(n)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            cnt = 0
            while not (i % 5):
                i //= 5
                cnt += 1
            ans += cnt
        return ans

# O(logn)：数学建模很关键啊
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while(n >= 5):
            n //= 5
            ans += n
        return ans