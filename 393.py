# 就按照题目叙述的情况来
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 0xxxxxxx: 0~127
        # 10xxxxxx: 128~191
        # 110xxxxx: 128+64=192, 192~223
        # 1110xxxx: 224~239
        # 11110xxx: 240~247
        def typenum(num: int) -> int:
            if num < 128:
                return 1
            elif num >= 192 and num < 224:
                return 2
            elif num >= 224 and num < 240:
                return 3
            elif num >= 240 and num < 248:
                return 4
            elif num >= 128 and num < 192:
                return 0
            else: return -1
        i = 0
        n = len(data)
        while(i < n):
            data_type = typenum(data[i])
            if data_type <= 0:
                return False
            for j in range(1, data_type):
                if i + j == n or typenum(data[i + j]) != 0:
                    return False
            i = i + data_type
        return True