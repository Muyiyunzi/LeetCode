class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        forward, backward, ans = [0]*n, [0]*n, []
        for i in range(1, n):
            if security[i] - security[i - 1] <= 0:
                forward[i] = forward[i - 1] + 1
            if security[n - i] - security[n - i - 1] >= 0:
                backward[n - i - 1] = backward[n - i] + 1
        for i in range(n):
            if forward[i] >= time and backward[i] >= time:
                ans.append(i)
        return ans
        