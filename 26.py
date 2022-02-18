# 第一遍垃圾版本
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i, j = 1, 1
#         while(j < len(nums)):
#             while(j < len(nums) and nums[j] == nums[j - 1]):
#                 j += 1
#             if j < len(nums):
#                 nums[i] = nums[j]
#                 i += 1
#                 j += 1
#         return i

# 优化版本
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        fast = slow = 1
        while(fast < len(nums)):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow