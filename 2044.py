class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_res, cnt = 0, 0
        def dfs(index, result):
            nonlocal max_res, cnt
            if index == n:
                if result > max_res:
                    max_res = result
                    cnt = 1
                elif result == max_res:
                    cnt += 1
            else:
                dfs(index+1, result | nums[index])
                dfs(index+1, result)
        dfs(0, 0)
        return cnt