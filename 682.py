# 第一版，现在写try except简直上瘾。。
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        q = []
        for i in ops:
            try:
                q.append(int(i))
            except ValueError:
                if i == 'C':
                    q.pop()
                elif i == 'D':
                    q.append(q[-1] * 2)
                elif i == '+':
                    q.append(q[-1] + q[-2])
        return sum(q)