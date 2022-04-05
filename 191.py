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
# 好吧也不一定。可能这种大数之间的按位与太耗时了
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n: # 每发生一次and操作，去掉一个1，直至全0
            n &= (n - 1)
            cnt += 1
        return cnt

# 用库函数的时间居然是和方法一一样的
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()