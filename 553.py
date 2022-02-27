# 直接求，必是最后除到底
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        ans = str(nums[0]) + '/'
        if n == 2:
            return ans + str(nums[1])
        ans += '('
        for i in range(1, n - 1):
            ans += str(nums[i]) + '/'
        ans += str(nums[-1]) + ')'
        return ans

# 第二版，这样的代码更优美一些
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        return str(nums[0]) + '/(' + "/".join(map(str, nums[1:])) + ')'

# 第三版 DP
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        dptable = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(2)]
        dpstr = [[['' for _ in range(n)] for _ in range(n)] for _ in range(2)]
        for i in range(n):
            dptable[0][i][i] = nums[i]
            dptable[1][i][i] = nums[i]
            dpstr[0][i][i] = str(nums[i])
            dpstr[1][i][i] = str(nums[i])
        for i in range(1, n):
            for j in range(n-i):
                Min = inf
                Max = 0
                index_min, index_max = 0, 0
                for k in range(i):
                    now_min = dptable[0][j][j+k] / dptable[1][j+k+1][j+i]
                    now_max = dptable[1][j][j+k] / dptable[0][j+k+1][j+i]
                    if now_min < Min:
                        Min = now_min
                        index_min = k                        
                    if now_max > Max:
                        Max = now_max
                        index_max = k
                dptable[0][j][j+i] = Min
                dptable[1][j][j+i] = Max
                if index_min == i - 1:
                    dpstr[0][j][j+i] = dpstr[0][j][j+index_min] + '/' + dpstr[1][j+index_min+1][j+i]
                else:
                    dpstr[0][j][j+i] = dpstr[0][j][j+index_min] + '/(' + dpstr[1][j+index_min+1][j+i] + ')'
                if index_max == i - 1:
                    dpstr[1][j][j+i] = dpstr[1][j][j+index_max] + '/' + dpstr[0][j+index_max+1][j+i]
                else:
                    dpstr[1][j][j+i] = dpstr[1][j][j+index_max] + '/(' + dpstr[0][j+index_max+1][j+i] + ')'
        return dpstr[1][0][n-1]