# 树状数组
class NumArray:
    # 初始化时，调用add方法
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(self.nums)
        self.tree = [0] * (self.length + 1) # 这里要+1就是为了避免x=0的循环情况
        for ind, val in enumerate(nums, 1):
            self.add(ind, val)            

    def add(self, index, val): # 向上检索，有关的全加一遍val，logn
        while(index < self.length + 1):
            self.tree[index] += val
            index += (index & -index)
        
    def update(self, index: int, val: int) -> None: # 更新时，不光要对tree更新差值，还要赋新的值上去
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumBefore(self, index): # 向下检索，之前的全部加起来，logn
        Sum = 0
        while(index > 0):
            Sum += self.tree[index]
            index -= (index & -index)
        return Sum

    def sumRange(self, left: int, right: int) -> int:
        return self.sumBefore(right + 1) - self.sumBefore(left) # 注意这里right+1，left不+
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)