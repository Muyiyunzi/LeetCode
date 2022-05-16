class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sumleft, sumright = 0, sum(nums)
        ans, n = 0, len(nums)
        for i in range(n-1):
            val = nums[i]
            sumleft += val
            sumright -= val
            if sumleft >= sumright:
                ans += 1
        return ans