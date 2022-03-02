# 离成功很接近了，用string会产生'020'这种尴尬的情况
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        L = len(n)
        ans = n[0:(L+1)//2]
        candidates = [10**L + 1, 10**(L-1)-1]
        if L % 2 == 1:
            for ans_int in range(int(ans) - 1, int(ans) + 2):
                s_new = str(ans_int // 10) + str(ans_int%10) + str(ans_int // 10)[::-1]
                candidates.append(int(s_new))
        else:
            for ans_int in range(int(ans) - 1, int(ans) + 2):
                s_new = str(ans_int) + str(ans_int)[::-1]
                candidates.append(int(s_new))
        ans = -1
        res = inf
        for candidate in candidates:
            res_new = abs(candidate - int(n))
            if res_new == 0: continue
            if res_new < res:
                res = res_new
                ans = candidate
            elif res_new == res and candidate < ans:
                ans = candidate
        return str(ans)

# 第一版
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        L = len(n)
        half = n[0:(L+1)//2]
        candidates = [10**L + 1, 10**(L-1)-1]
        for half_int in range(int(half) - 1, int(half) + 2):
            base = half_int * 10**((L+1)//2 - L%2)
            reverse = str(half_int)[-1 - L%2::-1]
            if reverse:
                candidates.append(base + int(reverse))
            else:
                candidates.append(base)
        ans = -1
        res = inf
        for candidate in candidates:
            res_new = abs(candidate - int(n))
            if res_new == 0: continue
            if res_new < res:
                res = res_new
                ans = candidate
            elif res_new == res and candidate < ans:
                ans = candidate
        return str(ans)