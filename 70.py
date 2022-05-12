stairs = [1, 1, 2]
for _ in range(43):
    stairs.append(stairs[-1] + stairs[-2])

class Solution:
    def climbStairs(self, n: int) -> int:
        return stairs[n]
