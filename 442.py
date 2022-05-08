class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            while nums[nums[i]-1] != nums[i]:
                val = nums[i]
                nums[i], nums[val-1] = nums[val-1], nums[i]

        for i, val in enumerate(nums):
            if val - 1 != i:
                ans.append(val)
        return ans
