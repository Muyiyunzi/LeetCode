# 早知两次遍历，就不想那么多花里胡哨的了。。。
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        n = len(s)
        pos = -n
        for i in range(n):
            if s[i] == c:
                pos = i
            ans.append(i-pos)
        pos = 2 * n
        for i in range(n-1, -1, -1):
            if s[i] == c:
                pos = i
            ans[i] = min(pos-i, ans[i])
        return ans