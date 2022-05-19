# 这里bisect用的好啊。其实前边开多大都无所谓，主要是比较规则要整明白
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def compKey(x):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(x // i, n)
            return cnt
        return bisect_left(range(m*n), k, key=compKey)