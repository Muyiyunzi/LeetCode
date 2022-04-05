# bin操作的时间复杂度O(log(n))，所以确实也是logn级别吧
class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)[2:]
        cnt = 0
        for i in list(s):
            if i == '1':
                cnt += 1
        return cnt

# n & n-1这种奇技淫巧常数应该更小一些？
