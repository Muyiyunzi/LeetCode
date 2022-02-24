# 第一版
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(n): # 考察第i号球
            row, col = 0, i
            while(row < m):
                if grid[row][col] == 1:
                    if col == n-1 or grid[row][col + 1] == -1:
                        ans.append(-1)
                        break
                    else:
                        col += 1  
                else:
                    if col == 0 or grid[row][col - 1] == 1:
                        ans.append(-1)
                        break
                    else:
                        col -= 1
                row += 1
            if row == m:
                ans.append(col)
        return ans

# 第二版
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [-1] * n
        for i in range(n): # 考察第i号球
            col = i
            for row in range(m):
                move = grid[row][col]
                col += move
                if col < 0 or col == n or grid[row][col] != move:
                    break
            else:
                ans[i] = col
        return ans