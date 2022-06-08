class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1 = points[0][0] - points[1][0]
        y1 = points[0][1] - points[1][1]
        x2 = points[1][0] - points[2][0]
        y2 = points[1][1] - points[2][1]
        if (x1 != 0 or y1 != 0) and (x2 != 0 or y2 != 0) and x1*y2 != x2*y1:
            return True
        return False