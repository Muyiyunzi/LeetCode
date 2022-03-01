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

# 找规律，O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if numRows == 1 or r > n:
            return s
        ans = []
        t = 2 * r - 2
        for i in range(r): # line
            for j in range(i, n, t):
                ans.append(s[j])
                if j + t - 2 * i < n and 0 < i < r - 1:
                    ans.append(s[j+t-2*i])
        return "".join(ans)