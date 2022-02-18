# 第一版
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        S_max = (r - l) * min(height[l], height[r])
        while(l < r):
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            S_now = (r - l) * min(height[l], height[r])
            if S_now > S_max:
                S_max = S_now
        return S_max

# 第二版
# 这样其实还是重复计算了很多次S
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        S_max = 0
        while(l < r):
            S_now = (r - l) * min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            S_max = max(S_max, S_now) # 放在if-else前后都可以
        return S_max

# 第三版 耗时更少，但代码量更多，占用空间应该也更多一些
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        S_max = 0
        while(l < r):
            S_now = (r - l) * min(height[l], height[r])
            S_max = max(S_max, S_now)
            if height[l] < height[r]:
                temp = height[l]
                while l < r and height[l] <= temp:
                    l += 1
            else:
                temp = height[r]
                while r > l and height[r] <= temp:
                    r -= 1
        return S_max