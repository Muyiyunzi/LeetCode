class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i, n = 0, len(nums)
        ans = []

        for i in range(n):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, n - 1  
            while(j < k):
                if nums[j] + nums[k] == -nums[i]:
                    ans.append([nums[i], nums[j], nums[k]])
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                    while(j < k and nums[k+1] == nums[k]):
                        k-=1
                    continue
                j += 1
                while(j < k and nums[j-1] == nums[j]):
                    j+=1
        return ans