# 注意打的表也可以取余
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        cnt, ans = 0, 1
        temp = pressedKeys[0]
        
        chart1 = [1, 2, 4]
        chart2 = [1, 2, 4, 8]
        for i in range(3, 100000):
            chart1.append((chart1[i-1] + chart1[i-2] + chart1[i-3])% (10**9 + 7))
        for i in range(4, 100000):
            chart2.append((chart2[i-1] + chart2[i-2] + chart2[i-3] + chart2[i-4])% (10**9 + 7))
        
        n = len(pressedKeys)
        
        def check(n):
            if temp in "79":
                res = chart2[cnt-1]
            else:
                res = chart1[cnt-1]
            return res
        
        for i, val in enumerate(pressedKeys):
            if val != temp:
                ans = ans * check(cnt) % (10**9 + 7)
                temp = val
                cnt = 1
            else:
                cnt += 1
                if i == n-1:
                    ans = ans * check(cnt) % (10**9 + 7)
        return ans


# 打表要学会放在前边
MOD = 10**9 + 7
f = [1,2,4]
g = [1,2,4,8]
for _ in range(10**5 - 2):
    f.append((f[-1] + f[-2] + f[-3]) % MOD)
    g.append((g[-1] + g[-2] + g[-3] + g[-4]) % MOD)

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        ans = 1
        for ch, grp in groupby(pressedKeys):
            n = len(list(grp)) - 1
            ans = ans * (g[n] if ch in "79" else f[n]) % MOD
        return ans