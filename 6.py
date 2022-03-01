# 二维矩阵直接模拟，O(rn)很慢
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        G = [['' for _ in range(len(s) // 2 + 1)] for _ in range(numRows)]
        i, j = 0, 0
        s = list(s)
        for ind, k in enumerate(s):
            G[i][j] = k
            if ind % (2*numRows - 2) < (numRows - 1):
                i += 1
            else:
                j += 1
                i -= 1
        ans = ''
        for i in G:
            for j in i:
                if j:
                    ans += j
        return ans
