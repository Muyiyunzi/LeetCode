class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        n = len(positions)
        heights = [0] * n
        for i, (left1, side1) in enumerate(positions):
            right1 = left1 + side1
            heights[i] = side1
            for j in range(i):
                left2, side2 = positions[j][0], positions[j][1]
                right2 = left2 + side2
                if left2 < right1 and right2 > left1:
                    heights[i] = max(heights[i], side1+heights[j])

        for i in range(1, n):
            heights[i] = max(heights[i], heights[i-1])
        
        return heights