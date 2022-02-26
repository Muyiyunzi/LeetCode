class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        Min = inf
        for i in range(len(nums)):
            if nums[i] > Min:
                ans = max(nums[i] - Min, ans)
            else:
                Min = min(Min, nums[i])
        return ans