# 随机快速排序，能够到达O(n)
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
    
    def quickSelected(self, nums, left, right, k):
        index = self.randomizedPartition(nums, left, right)
        if index == k:
            return nums[k]
        elif index < k:
            return self.quickSelected(nums, index + 1, right, k)
        else:
            return self.quickSelected(nums, left, index - 1, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelected(nums, 0, len(nums) - 1, len(nums) - k)

# 调用内部方法，O(nlogn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]