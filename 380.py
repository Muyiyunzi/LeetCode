# 变长数组+哈希表
class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        ind = self.index[val]
        self.vals[ind] = self.vals[-1]
        self.index[self.vals[-1]] = ind
        self.vals.pop()
        del self.index[val]
        return True

    def getRandom(self) -> int:
        return choice(self.vals)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()