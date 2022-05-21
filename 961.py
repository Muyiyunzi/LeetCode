class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = set()
        for i in nums:
            if i not in d:
                d.add(i)
            else:
                return i