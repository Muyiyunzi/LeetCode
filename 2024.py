# 滑窗，其实本质上也就是双指针，一定要像双指针一样明白滑动条件
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def findMaxLen(ch: str) -> int:
            left, ans, cnt = 0, 0, 0
            n = len(answerKey)
            for right in range(n):
                if answerKey[right] != ch:
                    cnt += 1
                while(cnt > k):
                    if answerKey[left] != ch:
                        cnt -= 1
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(findMaxLen('T'), findMaxLen('F'))