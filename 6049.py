# 坑点一是连续，再就是想hash可以用tuple！
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ans = set()
        n = len(nums)
        for i, val in enumerate(nums):
            j = i
            know = 0
            snow = []
            while(j < n):
                if nums[j] % p == 0:
                    if know == k:
                        break
                    else:
                        know += 1
                snow.append(nums[j])
                ans.add(tuple(snow))
                j += 1
        return len(ans)
            