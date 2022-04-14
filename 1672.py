# 常规模拟，有一点慢
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            temp = sum(i)
            ans = max(temp, ans)
        return ans 

# 试试巧用map函数最后取max：快一些，内存占用还小一点
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))