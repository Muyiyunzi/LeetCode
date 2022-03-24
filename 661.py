# 深度学习卷积，很简单的模拟题
# 看了一下，时间快的都是各种if-else判定，佛了，又臭又长，不过可以看出max min这些还是比较慢的
# 所以这个题还挺好的，另外可以学到ans那里的区别
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        ans = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                # 3x3
                Sum = 0
                cnt = 0
                for m in range(max(0, i - 1), min(row, i + 2)):
                    for n in range(max(0, j - 1), min(col, j + 2)):
                        Sum += img[m][n]
                        cnt += 1
                ans[i][j] = Sum // cnt
        return ans