# 76ms 超过了100%提交记录诶
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = {2, 3, 5, 7, 11, 13, 17, 19, 23}
        cnt = 0
        for i in range(left, right+1):
            if i.bit_count() in prime:
                cnt += 1
        return cnt