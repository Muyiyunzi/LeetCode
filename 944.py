# 第一版，排序肯定是耗时的
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        ans = 0
        for i in range(n):
            colstr = "".join(j[i] for j in strs)
            if "".join(sorted(colstr)) != colstr:
                ans += 1
        return ans

# 第二版，学会了zip(*)之后加pairwise和break就快多了，内存占用也少
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            for x, y in itertools.pairwise(col):
                if x > y:
                    ans += 1
                    break
        return ans