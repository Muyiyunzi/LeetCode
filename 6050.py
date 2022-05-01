# 动态规划，不难，一遍过
class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        ans = [0]
        exist = dict()
        for i in range(n):
            if s[i] in exist.keys():
                ans.append(ans[-1] + i - exist[s[i]])
            else:
                ans.append(ans[-1] + i + 1)
            exist[s[i]] = i
        return sum(ans)