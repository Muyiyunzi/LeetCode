# 第一版
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        len1, len2 = len(first), len(second)
        if len1 == len2: # 替换
            ans = 0
            for i in range(len1):
                if first[i] != second[i]:
                    ans += 1
                    if ans == 2:
                        return False
            return True
        
        elif len1 == len2 + 1: # 删除
            i, j = 0, 0
            while(i < len1 and j < len2):
                if first[i] != second[j]:
                    i += 1
                    continue
                i += 1
                j += 1
            if i - j >= 2:
                return False
            return True
        
        elif len1 == len2 - 1: # 删除
            i, j = 0, 0
            while(i < len1 and j < len2):
                if first[i] != second[j]:
                    j += 1
                    continue
                i += 1
                j += 1
            if j - i >= 2:
                return False
            return True

        else:
            return False

# 第二版，按答案的便捷方式修改
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        len1, len2 = len(first), len(second)
        if len1 < len2:
            return self.oneEditAway(second, first)
        if len1 > len2 + 1:
            return False
        for i, (a, b) in enumerate(zip(first, second)):
            if a != b:
                return first[i+1:] == second[i+1:] if len1 == len2 else first[i+1:] == second[i:]
        return True