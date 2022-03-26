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

# 第二版，按照答案写了一个if完后else的版本，另外新开了now而不是最后sum
# 时间更慢，空间还要多一点，anyway都是On
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        q = []
        ans = 0
        for i in ops:
            if i == 'C':
                ans -= q.pop()
                continue
            elif i == 'D':
                now = q[-1] * 2
            elif i == '+':
                now = q[-1] + q[-2]
            else:
                now = int(i)
            ans += now
            q.append(now)
        return ans