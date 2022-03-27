# 重点在于余数分摊，要不然常系数太大也容易超时
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        res = total - sum(rolls)
        ave = (res) / n
        if ave > 6 or ave < 1:
            return []
        # 那么必然有解
        ave_floor = int(ave)
        res_new = res - ave_floor * n
        ans = [ave_floor] * n
        for i in range(res_new):
            ans[i] += 1
        return ans