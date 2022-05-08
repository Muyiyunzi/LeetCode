# 后面学习一下@cache装饰器
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if not (m + n) % 2 or grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        @cache
        def dfs(x, y, status):
            if x == m-1 and y == n-1:
                return status==1

            status += 1 if grid[x][y] == '(' else -1
            
            if status < 0 or status > m - x + n - y - 2:
                return False
            
            return x+1<m and dfs(x+1, y, status) or y+1<n and dfs(x, y+1, status)
        
        return dfs(0, 0, 0)