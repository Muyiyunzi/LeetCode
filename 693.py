# 因为感觉可能的值不多，就先存一个哈希表出来
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        i = 1
        d = defaultdict(bool)
        for j in range(32):
            d[i] = True
            i = (i << 1) + (i + 1) % 2
        return d[n]

# 还是位运算直接判断更简洁一些
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        return a & (a + 1) == 0