
# 去重容易想不到

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        n, cnt = len(p), 1
        ans = [0] * 26
        ans[ord(p[0]) - 97] = 1
        for i in range(1, n):
            if ord(p[i]) == ord(p[i-1]) + 1 or (p[i] == 'a' and p[i-1] == 'z'):
                cnt += 1
                ans[ord(p[i]) - 97] = max(ans[ord(p[i]) - 97], cnt)
            else:
                cnt = 1
                ans[ord(p[i]) - 97] = max(ans[ord(p[i]) - 97], cnt)

        return sum(ans)