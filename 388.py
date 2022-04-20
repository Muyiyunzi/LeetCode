# 56ms 14.9MB
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        filesys = input.split('\n')
        length_level = {}
        maxlen = 0
        for i in filesys:
            level = i.count('\t')
            length_level[level] = len(i) - level + 1
            if level == 0:
                length_level[level] -= 1         
            if '.' in i: # 是文件
                maxlen = max(sum(list(length_level.values())[:level+1]), maxlen)
        return maxlen

# 32ms 15MB
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        filesys = input.split('\n')
        length_level = {-1: 0}
        maxlen = 0
        for i in filesys:
            level = i.count('\t')
            length_level[level] = length_level[level-1] + len(i) - level       
            if '.' in i: # 是文件
                maxlen = max(length_level[level] + level, maxlen) # 补'/'
        return maxlen

# 另外注意，如果不用split的话，\n\t其实都是一个字符。。