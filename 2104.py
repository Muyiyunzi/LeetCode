# 暴力双指针
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        Sum = 0
        for i in range(n-1):
            Max = Min = nums[i]
            for j in range(i+1, n):
                Max = max(Max, nums[j])
                Min = min(Min, nums[j])
                Sum += (Max - Min)
        return Sum
