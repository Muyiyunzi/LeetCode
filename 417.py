# DFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def search(start):
            visited = set()
            def dfs(x, y):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                    if 0 <= i < m and 0 <= j < n and heights[i][j] >= heights[x][y]:
                        dfs(i, j)
            for (x, y) in start:
                dfs(x, y)
            return visited

        pacific_start = [(0, x) for x in range(n)] + [(x, 0) for x in range(1, m)]
        atlantic_start = [(m-1, x) for x in range(n)] + [(x, n-1) for x in range(m - 1)]
        return list(map(list, search(pacific_start) & search(atlantic_start)))

# BFS 好像更快更省空间一些
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def bfs_search(start):
            visited = set()
            q = deque(start)
            while q:
                (x, y) = q.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                    if 0 <= i < m and 0 <= j < n and heights[i][j] >= heights[x][y]:
                        q.append((i, j))
            return visited

        pacific_start = [(0, x) for x in range(n)] + [(x, 0) for x in range(1, m)]
        atlantic_start = [(m-1, x) for x in range(n)] + [(x, n-1) for x in range(m - 1)]
        return list(map(list, bfs_search(pacific_start) & bfs_search(atlantic_start)))