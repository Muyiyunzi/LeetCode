# 超时
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i, val in enumerate(nums):
            j = i
            prod = 1
            while(j < n):
                prod *= nums[j]
                if prod < k:
                    ans += 1
                else:
                    break
                j += 1
        return ans

# 改滑窗
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 可能真的没法正序
        i, ans, prod = 0, 0, 1
        for j, val in enumerate(nums):
            prod *= nums[j]
            while(i <= j and prod >= k):
                prod /= nums[i]
                i += 1
            ans += j - i + 1
        return ans