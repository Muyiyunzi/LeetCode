# 关键是找第k个小/大的元素。关联题目215
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ave = sorted(nums)[len(nums) // 2]
        return sum(abs(i - ave) for i in nums)