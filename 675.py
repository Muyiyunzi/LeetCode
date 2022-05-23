# BFS寻路问题
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        m, n = len(forest), len(forest[0])

        # 记录路径
        path = []
        for x in range(m):
            for y in range(n):
                if forest[x][y] == 0 or forest[x][y] == 1:
                    continue
                path.append([forest[x][y], [x, y]])
        path.sort()

        p, trees, ans = 0, len(path), 0
        q = [[0, 0]]
        while p < trees:  # 下一步有树可砍
            if p != 0:
                q = [path[p-1][1]]
            cnt = 0
            vis = set()
            while q:
                if path[p][1] in q:
                    ans += cnt
                    break
                temp = q
                q = []
                for x, y in temp:
                    for xx, yy in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                        if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in vis and forest[xx][yy] != 0:
                            vis.add((xx, yy))
                            q.append([xx, yy])
                cnt += 1
            else:
                return -1
            p += 1
        return ans