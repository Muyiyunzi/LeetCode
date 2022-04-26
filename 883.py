# 小心0 不能一遍AC
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        s_xy, s_xz = 0, 0
        maxyz = defaultdict(int)
        for i in grid:
            s_xz += max(i)
            for ind, val in enumerate(i):
                maxyz[ind] = max(maxyz[ind], val)
                if val:
                    s_xy += 1
        s_yz = sum(maxyz.values())
        return s_xy + s_xz + s_yz