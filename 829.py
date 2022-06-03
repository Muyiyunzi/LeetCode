# 第一版，用了SUM+break
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        SUM = 0
        for i in range(1, 10**5):
            SUM += i
            if SUM > n:
                break
            if i % 2 == 1:
                ans += n % i == 0
            else:
                ans += ((n / i  - n // i) == 0.5)
        return ans

# 后来发现，break只要找到一个充分大的数，使其从1开始到的数sum起来大于n就行。
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        for i in range(1, int(sqrt(n*2))+1):
            if i % 2 == 1:
                ans += n % i == 0
            else:
                ans += ((n / i  - n // i) == 0.5)
        return ans