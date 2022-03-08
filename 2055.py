class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # 预设哈希左右盘子的位置这个没问题，但是对于query的处理在于：必须先找蜡烛，而不能遍历i数盘子，否则超时
        n = len(s)
        left, right = -1, n
        lefts, rights = [-1] * n, [n] * n
        plates_left = [0] * n
        plates = 0
        for i in range(n):
            if s[i] == '|':
                left = i
                plates_left[i] = plates
            else:
                plates += 1
            lefts[i] = left # 注意这里就不能加到else里去了，蜡烛的左/右方蜡烛也要更新
            if s[n - 1 - i] == '|':
                right = n - 1 - i
            rights[n - 1 - i] = right
        ans = []
        for (x, y) in queries:
            candle_x, candle_y = rights[x], lefts[y]              
            if candle_x < candle_y:
                ans.append(plates_left[candle_y] - plates_left[candle_x])
            else:
                ans.append(0)
        return ans
            
                