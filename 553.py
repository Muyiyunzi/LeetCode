# 直接求，必是最后除到底
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        ans = str(nums[0]) + '/'
        if n == 2:
            return ans + str(nums[1])
        ans += '('
        for i in range(1, n - 1):
            ans += str(nums[i]) + '/'
        ans += str(nums[-1]) + ')'
        return ans

# 第二版，这样的代码更优美一些
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        return str(nums[0]) + '/(' + "/".join(map(str, nums[1:])) + ')'