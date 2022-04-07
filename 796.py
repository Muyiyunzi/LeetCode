# 这样比较应该是O(n+n)，最坏情况O(n2)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            if s[i] == goal[0]:
                if s[:i] == goal[n-i:] and s[i:] == goal[:n-i]:
                    return True
        return False

# 更巧妙的是利用in的KMP算法，可以O(n)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s
