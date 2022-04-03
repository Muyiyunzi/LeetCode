# 第一版，单指针，奇怪的logn
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        n = len(letters)
        i = n // 2
        while(i > 0 and i < n):
            if letters[i - 1] <= target and target < letters[i]:
                break
            else:
                if letters[i] > target:
                    i //= 2
                else:
                    i += 1
        return letters[i]

# 第二版，双指针
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or letters[0] > target:
            return letters[0]
        n = len(letters)
        left, right = 0, n - 1
        while left < right - 1:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid
        return letters[right]
        