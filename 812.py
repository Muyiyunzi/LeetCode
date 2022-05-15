# 数学。凸包方法可以码住，后面再说
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        S = 0
        for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3):
            S = max(S, 0.5 * abs((x3-x1)*(y2-y1) + (y3-y1)*(x3-x2) - (x3-x1)*(y3-y1)))
        return S

# 答案还有行列式球三角形面积，也是很绝。