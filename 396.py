# 这题测时间还挺有趣的
# 第一版
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        fval = 0
        total = sum(nums)
        for i in range(n):
            fval += i * nums[i]
        ans = fval
        for i in range(n-1):
            fval = fval - total + n * nums[i]
            ans = max(ans, fval)
        return ans

# 第二版
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        res = cur = sum(idx * num for idx,num in enumerate(nums))
        total = sum(nums)
        n = len(nums)
        while nums:
            cur += total - nums.pop() * n
            res = cur if cur > res else res
        return res

# 结论：1.当ind和值都要用的时候，enumerate很快。2.pop确实会加速，但是只适用于用完即弃。3.max()会造成100ms左右的差异