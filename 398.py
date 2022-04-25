# 猴子
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(nums)

    def pick(self, target: int) -> int:
        ans = randint(0, self.length-1)
        while self.nums[ans] != target:
            ans = randint(0, self.length-1)
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# 哈希表
class Solution:

    def __init__(self, nums: List[int]):
        self.hashtable = defaultdict(list)
        for i, val in enumerate(nums):
            self.hashtable[val].append(i)

    def pick(self, target: int) -> int:
        return choice(self.hashtable[target])

# 水塘抽样
#速度上明显更快，内存消耗上也与猴子相当
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans, cnt = 0, 0
        for i, val in enumerate(self.nums):
            if val == target:
                x = randint(0, cnt)
                if not x:
                    ans = i
                cnt += 1
        return ans