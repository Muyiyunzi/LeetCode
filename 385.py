# 太坑啦，还是有可能有这种情况的，"[123,456,[788,799,833],[[]],10,[]]"
# 还是老老实实DFS或者递归吧
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        index = 0
        def dfs():
            nonlocal index
            if s[index] == '[':
                index += 1
                temp = NestedInteger()
                while(s[index] != ']'):
                    temp.add(dfs())
                    if s[index] == ',':
                        index += 1
                index += 1
                return temp
            else:
                negative = False
                if s[index] == '-':
                    negative = True
                    index += 1
                num = 0
                while(index < len(s) and s[index].isdigit()): # 这里可能会坑啊
                    num *= 10
                    num += int(s[index])
                    index += 1
                if negative:
                    num = -num
                return NestedInteger(num)

        return dfs()
