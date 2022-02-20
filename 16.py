class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = inf
        for i in range(n - 2):
            j, k = i + 1, n - 1
            Sum = nums[i] + nums[j] + nums[k]
            while(j < k):
                res_new = Sum - target
                if abs(res_new) < abs(res):
                    res = res_new
                if Sum > target:
                    k -= 1
                    Sum = Sum - nums[k + 1] + nums[k]
                elif Sum < target:
                    j += 1
                    Sum = Sum - nums[j - 1] + nums[j]
                else:
                    return target
        return res + target