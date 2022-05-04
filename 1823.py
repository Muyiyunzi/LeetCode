# 约瑟夫问题，注意推导递推公式的时候要记得重新编号
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return 1 if n==1 else (self.findTheWinner(n-1, k) + k - 1) % n + 1

# 改成迭代，空间减少但是时间上升
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 1
        for i in range(2, n + 1):
            winner = (winner + k - 1) % i + 1
        return winner