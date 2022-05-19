# 很好的联系排序的题目呀

# 快速排序
class Solution:
    def randomizedPartition(self, nums, left, right):
        pivot = random.randint(left, right)
        nums[right], nums[pivot] = nums[pivot], nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] < nums[right]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i
    
    def randomizedQuickSort(self, nums, left, right):
        if left >= right:
            return
        index = self.randomizedPartition(nums, left, right)
        self.randomizedQuickSort(nums, left, index - 1)
        self.randomizedQuickSort(nums, index + 1, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomizedQuickSort(nums, 0, len(nums) - 1)
        return nums