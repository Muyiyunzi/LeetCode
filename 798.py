# 暴力O(n2)，超时了
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        ans, score = 0, 0
        n = len(nums)
        for k in range(n):
            cnt = 0
            for j in range(k):
                if nums[j] <= j + n - k:
                    cnt += 1
            for j in range(k, n):
                if nums[j] <= j - k:
                    cnt += 1
            if cnt > score:
                score = cnt
                ans = k
        return ans

# 差分O(n)，注意points没有被显式地存储，只需要计算差分数组即可
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = [0] * n
        for i, num in enumerate(nums):
            low = i + 1
            high = (i - num + n + 1) % n # 注意差分数组这里要+1
            if low != n: # 注意这里不判定，前边low那里加mod也可以，效果相同
                diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
        score, maxScore, ind = 0, 0, 0
        for i, diff in enumerate(diffs):
            score += diff
            if score > maxScore:
                maxScore = score
                ind = i
        return ind
