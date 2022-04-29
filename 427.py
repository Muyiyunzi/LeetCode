"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def checkleaf(x: int, y: int, side: int) -> 'Node':
            if all(grid[i][j] == grid[x][y] for i in range(x, x+side) for j in range(y, y+side)):
                return Node(grid[x][y], True)
            side //= 2
            topleft = checkleaf(x, y, side)
            topright = checkleaf(x, y+side, side)
            bottomleft = checkleaf(x+side, y, side)
            bottomright = checkleaf(x+side, y+side, side)
            return Node(True, False, topleft, topright, bottomleft, bottomright)
        return checkleaf(0, 0, len(grid))