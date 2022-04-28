# 感觉开两个数组是时间上最快的？打败了96%
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in nums:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        return even + odd

# 还有人用lambda的，很秀啊
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2 != 0)