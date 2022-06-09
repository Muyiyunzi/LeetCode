# 答案是用前缀和+二分查找的方式完成的。
# 像这种判断某个值在一堆区间里的哪个区间里时可以通过二分查找完成，虽不像哈希一样O(1)但也有O(logn)，很不错了
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.candidates = []
        self.weights = []
        for rect in rects:
            rect[0], rect[1] = ceil(rect[0]), ceil(rect[1])
            rect[2], rect[3] = floor(rect[2]), floor(rect[3])
            self.candidates.append(rect)
            self.weights.append((rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1))

    def pick(self) -> List[int]:
        rect = random.choices(self.candidates, self.weights)[0]
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()